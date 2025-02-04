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

# AudioSettings

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

Controls the global audio settings from script.

Setup speaker output and format.

### Static Properties

[driverCapabilities](AudioSettings-driverCapabilities.html)| Returns the
speaker mode capability of the current audio driver. (Read Only)  
---|---  
[dspTime](AudioSettings-dspTime.html)| Returns the current time of the audio
system.  
[outputSampleRate](AudioSettings-outputSampleRate.html)| Get the mixer's
current output rate.  
[speakerMode](AudioSettings-speakerMode.html)|  AudioSettings.speakerMode is
deprecated. Use AudioSettings.GetConfiguration and AudioSettings.Reset to
adjust audio settings instead.  
  
### Static Methods

[GetConfiguration](AudioSettings.GetConfiguration.html)| Returns the current
configuration of the audio device and system. The values in the struct may
then be modified and reapplied via AudioSettings.Reset.  
---|---  
[GetDSPBufferSize](AudioSettings.GetDSPBufferSize.html)| Get the mixer's
buffer size in samples.  
[GetSpatializerPluginName](AudioSettings.GetSpatializerPluginName.html)|
Returns the name of the spatializer selected on the currently-running
platform.  
[GetSpatializerPluginNames](AudioSettings.GetSpatializerPluginNames.html)|
Returns an array with the names of all the available spatializer plugins.  
[Reset](AudioSettings.Reset.html)| Changes the device configuration and
invokes the AudioSettings.OnAudioConfigurationChanged delegate with the
argument deviceWasChanged=false. There's no guarantee that the exact settings
specified are used, but Unity automatically uses the closest match that it
supports. Note: This can cause main thread stalls if AudioSettings.Reset is
called when objects are loading asynchronously.  
[SetSpatializerPluginName](AudioSettings.SetSpatializerPluginName.html)| Sets
the spatializer plugin for all platform groups. If a null or empty string is
passed in, the existing spatializer plugin will be cleared.  
  
### Events

[OnAudioConfigurationChanged](AudioSettings.OnAudioConfigurationChanged.html)|
A delegate called whenever the global audio settings are changed, either by
AudioSettings.Reset or by an external factor such as the OS control panel
changing the sample rate or because the default output device was changed, for
example when plugging in an HDMI monitor or a USB headset.  
---|---  
  
### Delegates

[AudioConfigurationChangeHandler](AudioSettings.AudioConfigurationChangeHandler.html)|
A delegate called whenever the global audio settings are changed, either by
AudioSettings.Reset or by an external device change such as the OS control
panel changing the sample rate or because the default output device was
changed, for example when plugging in an HDMI monitor or a USB headset.  
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

