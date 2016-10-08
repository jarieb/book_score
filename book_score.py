import sys, os
from labMTsimple.storyLab import *
import codecs ## handle utf8
import glob
from textstat.textstat import textstat as ts
from natsort import natsorted
import argparse

WORDS_PAGE = 250

def split_pages(text, page_words=WORDS_PAGE):

  paragraphs = text.split("\n\n")

  pages = []
  working = ''
  for para in paragraphs:
    working = working + para
    if ts.lexicon_count(working) >= page_words:
      pages.append(working)
      working = ''
  
  if not ts.lexicon_count(working) == 0:
    pages.append(working)

  return pages

def score_pages(pages,labMT,labMTvector,labMTwordList):

  scores = []
  for page in pages:

    pageValence, pageFvec = emotion(page,labMT,shift=True,happsList=labMTvector)

    pageStoppedVec = stopper(pageFvec,labMTvector,labMTwordList,stopVal=1.0)

    scores.append(emotionV(pageStoppedVec,labMTvector))

  return scores

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Book Stats Generator')
  parser.add_argument('-d', '--dir', required = True, help="Directory with the book text files in it")
  parser.add_argument('-w', '--words_page', required = False, type=int, default=WORDS_PAGE,help="The number of words per page")
  args = parser.parse_args()
  lang = 'english'

  args.dir = args.dir.rstrip('/')

  labMT,labMTvector,labMTwordList = emotionFileReader(stopval=0.0,lang=lang,returnVector=True)

  fout = open('book_stats_'+args.dir+'.csv','w')
  fout1 = open('page_sparklines_'+args.dir+'.csv','w')

  fout.write('chapter,WC,RL,HS\n')
  fout1.write('Page Happiness\n')
  for fname in natsorted(glob.glob(args.dir+'/*.txt')):
    f = codecs.open(fname,'r','utf8')
    chapter = f.read()
    f.close()
    chapter_name = fname.split(args.dir+'/')[1].split('.txt')[0]
  
    ## compute valence score and return frequency vector for generating wordshift
    chapterValence, chapterFvec = emotion(chapter,labMT,shift=True,happsList=labMTvector)

    ## but we didn't apply a lens yet, so stop the vectors first
    chapterStoppedVec = stopper(chapterFvec,labMTvector,labMTwordList,stopVal=1.0)

    chapterValence = emotionV(chapterStoppedVec,labMTvector)

    # Chapters less than WORD_PAGE should be ignored

    if ts.lexicon_count(chapter) < WORDS_PAGE:
      fout.write(('"{}",,,\n'.format(chapter_name)))
      text = ''
    else:
      fout.write(('"{}",{},{},{}\n'.format(chapter_name,ts.lexicon_count(chapter),ts.automated_readability_index(chapter),round(chapterValence,2))))
      text = ','.join(format(x, "1.1f") for x in score_pages(split_pages(chapter,args.words_page),labMT,labMTvector,labMTwordList))
    
    fout1.write(text+"\n")