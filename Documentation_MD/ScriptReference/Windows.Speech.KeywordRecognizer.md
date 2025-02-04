[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# KeywordRecognizer

class in UnityEngine.Windows.Speech

/

Inherits
from:[Windows.Speech.PhraseRecognizer](Windows.Speech.PhraseRecognizer.html)

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

KeywordRecognizer listens to speech input and attempts to match uttered
phrases to a list of registered keywords.

There can be many keyword recognizers active at any given time, but no two
keyword recognizers may be listening for the same keyword.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Text;
    using UnityEngine;
    using UnityEngine.Windows.Speech;  
      
    public class KeywordScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[SerializeField](SerializeField.html)]
        private string[] m_Keywords;  
      
        private [KeywordRecognizer](Windows.Speech.KeywordRecognizer.html) m_Recognizer;  
      
        void Start()
        {
            m_Recognizer = new [KeywordRecognizer](Windows.Speech.KeywordRecognizer.html)(m_Keywords);
            m_Recognizer.OnPhraseRecognized += OnPhraseRecognized;
            m_Recognizer.Start();
        }  
      
        private void OnPhraseRecognized([PhraseRecognizedEventArgs](Windows.Speech.PhraseRecognizedEventArgs.html) args)
        {
            StringBuilder builder = new StringBuilder();
            builder.AppendFormat("{0} ({1}){2}", args.text, args.confidence, Environment.NewLine);
            builder.AppendFormat("\tTimestamp: {0}{1}", args.phraseStartTime, Environment.NewLine);
            builder.AppendFormat("\tDuration: {0} seconds{1}", args.phraseDuration.TotalSeconds, Environment.NewLine);
            [Debug.Log](Debug.Log.html)(builder.ToString());
        }
    }
    

Keyword recognizer is currently functional only on Windows 10.

### Properties

[Keywords](Windows.Speech.KeywordRecognizer.Keywords.html)| Returns the list
of keywords which was supplied when the keyword recognizer was created.  
---|---  
  
### Constructors

[KeywordRecognizer](Windows.Speech.KeywordRecognizer-ctor.html)| Create a
KeywordRecognizer which listens to specified keywords with the specified
minimum confidence. Phrases under the specified minimum level will be ignored.  
---|---  
  
### Inherited Members

### Properties

[IsRunning](Windows.Speech.PhraseRecognizer.IsRunning.html)| Tells whether the
phrase recognizer is listening for phrases.  
---|---  
  
### Public Methods

[Dispose](Windows.Speech.PhraseRecognizer.Dispose.html)| Disposes the
resources used by phrase recognizer.  
---|---  
[Start](Windows.Speech.PhraseRecognizer.Start.html)| Makes the phrase
recognizer start listening to phrases.  
[Stop](Windows.Speech.PhraseRecognizer.Stop.html)| Stops the phrase recognizer
from listening to phrases.  
  
### Events

[OnPhraseRecognized](Windows.Speech.PhraseRecognizer.OnPhraseRecognized.html)|
Event that gets fired when the phrase recognizer recognizes a phrase.  
---|---  
  
### Delegates

[PhraseRecognizedDelegate](Windows.Speech.PhraseRecognizer.PhraseRecognizedDelegate.html)|
Delegate for OnPhraseRecognized event.  
---|---  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

