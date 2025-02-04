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

# GrammarRecognizer

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

The GrammarRecognizer is a complement to the KeywordRecognizer. In many cases
developers will find the KeywordRecognizer fills all their development needs.
However, in some cases, more complex grammars will be better expressed in the
form of an xml file on disk. The GrammarRecognizer uses Extensible Markup
Language (XML) elements and attributes, as specified in the World Wide Web
Consortium (W3C) Speech Recognition Grammar Specification (SRGS) Version 1.0.
These XML elements and attributes represent the rule structures that define
the words or phrases (commands) recognized by speech recognition engines.

For more information on this format, refer to [www.w3.org/TR/speech-
grammar](http://www.w3.org/TR/speech-grammar/) or on MSDN.  
  
There can be many grammar recognizers active at any given point in time, but
no two grammar recognizers may use the same grammar file.  
  
Grammar recognizer is currently functional only on Windows 10.

### Properties

[GrammarFilePath](Windows.Speech.GrammarRecognizer.GrammarFilePath.html)|
Returns the grammar file path which was supplied when the grammar recognizer
was created.  
---|---  
  
### Constructors

[GrammarRecognizer](Windows.Speech.GrammarRecognizer-ctor.html)| Creates a
grammar recognizer using specified file path and minimum confidence.  
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

