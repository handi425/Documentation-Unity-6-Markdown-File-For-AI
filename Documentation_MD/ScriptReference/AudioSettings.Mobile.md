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

# Mobile

class in UnityEngine

/

Implemented in:[UnityEngine.AudioModule](UnityEngine.AudioModule.html)

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

[Switch to Manual](../Manual/class-AudioSettings.html "Go to AudioSettings
Component in the Manual")

### Description

This class encapsulates properties and methods to handle audio output thread
on iOS/Android.

You may be able to reduce the power consumption of your app or game by using
this class. In general, for apps with simple looped music and short sound
effects, you should set
[AudioSettings.Mobile.stopAudioOutputOnMute](AudioSettings.Mobile-
stopAudioOutputOnMute.html) to true, and also call
[AudioSettings.Mobile.StopAudioOutput](AudioSettings.Mobile.StopAudioOutput.html)
if the user of your app sets music/sound volume to 0 in game settings. This
helps to reduce power consumption on most mobile devices. Also you can check
[AudioSettings.Mobile.muteState](AudioSettings.Mobile-muteState.html) property
and listen to
[AudioSettings.Mobile.OnMuteStateChanged](AudioSettings.Mobile.OnMuteStateChanged.html)
event to stop/start audio output thread when required.  
  
However, if your game or app has more complex sound or music logic, doing this
could cause synchronization issues. In particular, any sounds playing when
output is stopped are resumed from the same position when output is restarted,
and so may be out of sync with any gameplay code that continued to run during
that time. Therefore this setting may not be suitable if you are relying on
gameplay elements that should be synchronized with parts of audio that may be
continuing to play during output being switched off or on.

### Static Properties

[audioOutputStarted](AudioSettings.Mobile-audioOutputStarted.html)| Returns
true if audio output thread is working.  
---|---  
[muteState](AudioSettings.Mobile-muteState.html)| Returns true if current
device media volume is 0.  
[stopAudioOutputOnMute](AudioSettings.Mobile-stopAudioOutputOnMute.html)| Set
this property to true to make audio output thread automatically stop when
device media volume is set to 0 and to start it again when volume is not 0.  
  
### Static Methods

[StartAudioOutput](AudioSettings.Mobile.StartAudioOutput.html)| Starts audio
output thread on Android/iOS.  
---|---  
[StopAudioOutput](AudioSettings.Mobile.StopAudioOutput.html)| Stops audio
thread on Android/iOS.  
  
### Events

[OnMuteStateChanged](AudioSettings.Mobile.OnMuteStateChanged.html)| A delegate
called whenever the device mute state is changed.  
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

