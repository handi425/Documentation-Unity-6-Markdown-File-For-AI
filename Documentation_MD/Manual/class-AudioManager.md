[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AudioManager.html)
  * [中文](/cn/current/Manual/class-AudioManager.html)
  * [日本語](/ja/current/Manual/class-AudioManager.html)
  * [한국어](/kr/current/Manual/class-AudioManager.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AudioManager.html)
  * [中文](/cn/current/Manual/class-AudioManager.html)
  * [日本語](/ja/current/Manual/class-AudioManager.html)
  * [한국어](/kr/current/Manual/class-AudioManager.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Project Settings](comp-ManagerGroup.html)
  * Audio

[](class-ProjectSettingsWindow.html)

Use the Project Settings window

[](class-EditorManager.html)

Editor

# Audio

The **Audio** settings (main menu: **Edit** > **Project Settings** , then
select the **Audio** category) allows you to tweak the maximum volume of all
sounds playing in the scene.

![Audio settings](../uploads/Main/AudioSet.png) Audio settings **Property** | **Function**  
---|---  
**Global Volume** | Set the volume for all sounds during playback.  
**Volume Rolloff Scale** | Set the global attenuation rolloff factor for [Logarithmic rolloff-based sources](class-AudioSource.html). The higher the value, the faster the volume attenuates. Conversely, the lower the value, the slower it attenuates.   
**Tip:** A value of 1 simulates the “real world”.  
**Doppler Factor** | Set how audible the Doppler effect is. Use 0 to disable it. Use 1 make it audible for fast moving objects.  
**Tip:** After setting the **Doppler Factor** to 1, you can tweak both **Speed
of Sound** and **Doppler Factor** until you are satisfied.  
**Default Speaker Mode** | Set which speaker mode should be the default for your project. The default is 2, which corresponds to stereo speakers. For the full list of modes, see the [AudioSpeakerMode](../ScriptReference/AudioSpeakerMode.html) API reference.  
**Note:** You can also change the speaker mode at runtime through scripting.
See [Audio Settings](../ScriptReference/AudioSettings.html) for details.  
**System Sample Rate** | Set the output sample rate. If set to 0, Unity uses the sample rate of the system.   
**Note:** This only serves as a reference only, since certain platforms allow
you to change the sample rate, such as iOS or Android.  
**DSP Buffer Size** | Set the size of the DSP buffer to optimize for latency or performance.  
| **Default** | Default buffer size.  
| **Best Latency** | Trade off performance in favour of latency.  
| **Good Latency** | Balance between latency and performance.  
| **Best Performance** | Trade off latency in favour of performance.  
**Max Virtual Voices** | Set the number of virtual voices that the audio system manages. This value should always be larger than the number of voices played by the game. If not, Unity displays warnings in the console.  
**Max Real Voices** | Set the number of real voices that can play at the same time. At every frame, the loudest voice is picked.  
**Spatializer Plugin** | Choose which native audio plugin to use in order to perform spatialized filtering of 3D sources.  
**Ambisonic Decoder Plugin** | Choose which native audio plugin to perform ambisonic-to-binaural filtering of sources.  
**Disable Unity Audio** | Enable to deactivate the audio system in standalone builds.   
In the Editor the audio system is still on and supports previewing audio
clips, but Unity does not handle calls to
[AudioSource.Play](../ScriptReference/AudioSource.Play.html) and
[AudioSource.playOnAwake](../ScriptReference/AudioSource-playOnAwake.html) in
order to simulate behavior of the standalone build.  
**Virtualize Effect** | Enable to dynamically turn off effects and spatializers on AudioSources that are culled in order to save CPU.  
  
AudioManager

[](class-ProjectSettingsWindow.html)

Use the Project Settings window

[](class-EditorManager.html)

Editor

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

