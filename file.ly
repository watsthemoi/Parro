\version "2.24" 
\include "lilypond-book-preamble.ly"
    
color = #(define-music-function (parser location color) (string?) #{
        \once \override NoteHead #'color = #(x11-color color)
        \once \override Stem #'color = #(x11-color color)
        \once \override Rest #'color = #(x11-color color)
        \once \override Beam #'color = #(x11-color color)
     #})
    
\header { 
 
  } 
 
\score  { 
 
      << \new Staff  = bafbyfyafc { 
               << \new Voice { r 1  
                      ees' 4  
                      ees' 4  ~  
                       } 
                     
 
                \new Voice { r 2  
                      r 8.  
                      fis,, 8  
                      r 4  
                      b,, 16  
                      r 32  
                       } 
                     
 
                 >>
               
             \clef "treble" 
             \time 4/4
             \bar "|"  %{ end measure 1 %} 
             ees' 4  
             r 32  
             c' 8  
             c' 8  
             c' 8  
             c' 8  
             r 8  
             < g''  g'  > 8   
             < g''  g'  > 8   
             r 8  
             < g'  g''  > 8   
             \bar "|"  %{ end measure 2 %} 
             
               << \new Voice { g' 16  
                      r 4  
                      bes 4  
                      r 8  
                      bes 8.  
                      r 4  
                       } 
                     
 
                \new Voice { r 4..  
                      bes 8  
                      r 4..  
                       } 
                     
 
                 >>
               
             \bar "|"  %{ end measure 3 %} 
             
               << \new Voice { b' 8  
                      r 8  
                      b' 8  
                      bes' 8  
                      r 8  
                      bes' 8  
                      bes' 8  
                      bes' 8  
                      r 2  
                       } 
                     
 
                \new Voice { r 16  
                      b' 8  
                      r 1  
                       } 
                     
 
                 >>
               
             \bar "|."  %{ end measure 4 %} 
              } 
            
 
        >>
      
  } 
 
\paper { }
