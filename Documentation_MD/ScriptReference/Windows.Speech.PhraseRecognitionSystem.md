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

# PhraseRecognitionSystem

class in UnityEngine.Windows.Speech

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

Phrase recognition system is responsible for managing phrase recognizers and
dispatching recognition events to them.

In order for any phrase recognizers to recognize a phrase,
PhraseRecognitionSystem must be running. Starting a phrase recognition will
automatically start the phrase recognition system if it's stopped.  
  
Phrase recognition system cannot be started if there are any dictation
recognizers active.  
  
Phrase recognition system is currently only functional on Windows 10. Use
PhraseRecognitionSystem.isSupported property to determine whether speech
recognition is supported on the system that the application is running on.

### Static Properties

[isSupported](Windows.Speech.PhraseRecognitionSystem-isSupported.html)|
Returns whether speech recognition is supported on the machine that the
application is running on.  
---|---  
[Status](Windows.Speech.PhraseRecognitionSystem.Status.html)| Returns the
current status of the phrase recognition system.  
  
### Static Methods

[Restart](Windows.Speech.PhraseRecognitionSystem.Restart.html)| Attempts to
restart the phrase recognition system.  
---|---  
[Shutdown](Windows.Speech.PhraseRecognitionSystem.Shutdown.html)| Shuts phrase
recognition system down.  
  
### Events

[OnError](Windows.Speech.PhraseRecognitionSystem.OnError.html)| Event that
gets invoked when phrase recognition system encounters an error.  
---|---  
[OnStatusChanged](Windows.Speech.PhraseRecognitionSystem.OnStatusChanged.html)|
Event which occurs when the status of the phrase recognition system changes.  
  
### Delegates

[ErrorDelegate](Windows.Speech.PhraseRecognitionSystem.ErrorDelegate.html)|
Delegate for OnError event.  
---|---  
[StatusDelegate](Windows.Speech.PhraseRecognitionSystem.StatusDelegate.html)|
Delegate for OnStatusChanged event.  
  
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

