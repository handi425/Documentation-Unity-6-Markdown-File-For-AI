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

# DictationRecognizer

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

DictationRecognizer listens to speech input and attempts to determine what
phrase was uttered.

Users can register and listen for hypothesis and phrase completed events.
Start() and Stop() methods respectively enable and disable dictation
recognition. Once done with the recognizer, it must be disposed using
Dispose() method to release the resources it uses. It will release these
resources automatically during garbage collection at an additional performance
cost if they are not released prior to that.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UI;
    using UnityEngine.Windows.Speech;  
      
    public class DictationScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[SerializeField](SerializeField.html)]
        private Text m_Hypotheses;  
      
        [[SerializeField](SerializeField.html)]
        private Text m_Recognitions;  
      
        private [DictationRecognizer](Windows.Speech.DictationRecognizer.html) m_DictationRecognizer;  
      
        void Start()
        {
            m_DictationRecognizer = new [DictationRecognizer](Windows.Speech.DictationRecognizer.html)();  
      
            m_DictationRecognizer.DictationResult += (text, confidence) =>
            {
                [Debug.LogFormat](Debug.LogFormat.html)("Dictation result: {0}", text);
                m_Recognitions.text += text + "\n";
            };  
      
            m_DictationRecognizer.DictationHypothesis += (text) =>
            {
                [Debug.LogFormat](Debug.LogFormat.html)("Dictation hypothesis: {0}", text);
                m_Hypotheses.text += text;
            };  
      
            m_DictationRecognizer.DictationComplete += (completionCause) =>
            {
                if (completionCause != [DictationCompletionCause.Complete](Windows.Speech.DictationCompletionCause.Complete.html))
                    [Debug.LogErrorFormat](Debug.LogErrorFormat.html)("Dictation completed unsuccessfully: {0}.", completionCause);
            };  
      
            m_DictationRecognizer.DictationError += (error, hresult) =>
            {
                [Debug.LogErrorFormat](Debug.LogErrorFormat.html)("Dictation error: {0}; HResult = {1}.", error, hresult);
            };  
      
            m_DictationRecognizer.Start();
        }
    }
    

Dictation recognizer is currently functional only on Windows 10, and requires
that dictation is permitted in the user's Speech privacy policy
(Settings->Privacy->Speech, inking & typing). If dictation is not enabled,
DictationRecognizer will fail on
[Start](Windows.Speech.DictationRecognizer.Start.html). Developers can handle
this failure in an app-specific way by providing a
[DictationError](Windows.Speech.DictationRecognizer.DictationError.html)
delegate and testing for SPERR_SPEECH_PRIVACY_POLICY_NOT_ACCEPTED
(0x80045509).

### Properties

[AutoSilenceTimeoutSeconds](Windows.Speech.DictationRecognizer.AutoSilenceTimeoutSeconds.html)|
The time length in seconds before dictation recognizer session ends due to
lack of audio input.  
---|---  
[InitialSilenceTimeoutSeconds](Windows.Speech.DictationRecognizer.InitialSilenceTimeoutSeconds.html)|
The time length in seconds before dictation recognizer session ends due to
lack of audio input in case there was no audio heard in the current session.  
[Status](Windows.Speech.DictationRecognizer.Status.html)| Indicates the status
of dictation recognizer.  
  
### Constructors

[DictationRecognizer](Windows.Speech.DictationRecognizer-ctor.html)| Create a
DictationRecognizer with the specified minimum confidence and dictation topic
constraint. Phrases under the specified minimum level will be ignored.  
---|---  
  
### Public Methods

[Dispose](Windows.Speech.DictationRecognizer.Dispose.html)| Disposes the
resources this dictation recognizer uses.  
---|---  
[Start](Windows.Speech.DictationRecognizer.Start.html)| Starts the dictation
recognization session. Dictation recognizer can only be started if
PhraseRecognitionSystem is not running.  
[Stop](Windows.Speech.DictationRecognizer.Stop.html)| Stops the dictation
recognization session.  
  
### Events

[DictationComplete](Windows.Speech.DictationRecognizer.DictationComplete.html)|
Event that is triggered when the recognizer session completes.  
---|---  
[DictationError](Windows.Speech.DictationRecognizer.DictationError.html)|
Event that is triggered when the recognizer session encouters an error.  
[DictationHypothesis](Windows.Speech.DictationRecognizer.DictationHypothesis.html)|
Event that is triggered when the recognizer changes its hypothesis for the
current fragment.  
[DictationResult](Windows.Speech.DictationRecognizer.DictationResult.html)|
Event indicating a phrase has been recognized with the specified confidence
level.  
  
### Delegates

[DictationCompletedDelegate](Windows.Speech.DictationRecognizer.DictationCompletedDelegate.html)|
Delegate for DictationComplete event.  
---|---  
[DictationErrorHandler](Windows.Speech.DictationRecognizer.DictationErrorHandler.html)|
Delegate for DictationError event.  
[DictationHypothesisDelegate](Windows.Speech.DictationRecognizer.DictationHypothesisDelegate.html)|
Callback indicating a hypothesis change event. You should register with
DictationHypothesis event.  
[DictationResultDelegate](Windows.Speech.DictationRecognizer.DictationResultDelegate.html)|
Callback indicating a phrase has been recognized with the specified confidence
level. You should register with DictationResult event.  
  
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

