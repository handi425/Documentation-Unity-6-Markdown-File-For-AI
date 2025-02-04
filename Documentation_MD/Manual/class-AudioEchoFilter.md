[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AudioEchoFilter.html)
  * [中文](/cn/current/Manual/class-AudioEchoFilter.html)
  * [日本語](/ja/current/Manual/class-AudioEchoFilter.html)
  * [한국어](/kr/current/Manual/class-AudioEchoFilter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AudioEchoFilter.html)
  * [中文](/cn/current/Manual/class-AudioEchoFilter.html)
  * [日本語](/ja/current/Manual/class-AudioEchoFilter.html)
  * [한국어](/kr/current/Manual/class-AudioEchoFilter.html)

  * [Audio](Audio.html)
  * [Audio Reference](AudioReference.html)
  * [Audio Filters](class-AudioEffect.html)
  * Audio Echo Filter

[](class-AudioHighPassFilter.html)

Audio High Pass Filter

[](class-AudioDistortionFilter.html)

Audio Distortion Filter

# Audio Echo Filter

[Switch to Scripting](../ScriptReference/AudioEchoFilter.html "Go to
AudioEchoFilter page in the Scripting Reference")

The **Audio Echo Filter** repeats a sound after a given **Delay** ,
attenuating the repetitions based on the **Decay Ratio**.

## Properties

![](../uploads/Main/AudioEchoFilter.png) **_Property:_** | **_Function:_**  
---|---  
**Delay** | Echo delay in ms. 10 to 5000. Default = 500.  
**Decay Ratio** | Echo decay per delay. 0 to 1. 1.0 = No decay, 0.0 = total decay (ie simple 1 line delay). Default = 0.5.L  
**Wet Mix** | Volume of echo signal to pass to output. 0.0 to 1.0. Default = 1.0.  
**Dry Mix** An audio setting that allows you to set the volume of the original
signal to pass to output.  
See in [Glossary](Glossary.html#DryMix) | Volume of original signal to pass to output. 0.0 to 1.0. Default = 1.0.  
  
## Details

The **Wet Mix** value determines the amplitude of the filtered signal, where
the **Dry Mix** determines the amplitude of the unfiltered sound output.

Hard surfaces reflects the propagation of sound. For example a large canyon
can be made more convincing with the Audio Echo Filter.

Sound propagates slower than light - we all know that from lightning and
thunder. To simulate this, add an Audio Echo Filter to an event sound, set the
Wet Mix to 0.0 and modulate the Delay to the distance between
[AudioSource](class-AudioSource.html) and [AudioListener](class-
AudioListener.html).

AudioEchoFilter

[](class-AudioHighPassFilter.html)

Audio High Pass Filter

[](class-AudioDistortionFilter.html)

Audio Distortion Filter

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

