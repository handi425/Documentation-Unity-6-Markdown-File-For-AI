[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AudioPitchShifterEffect.html)
  * [中文](/cn/current/Manual/class-AudioPitchShifterEffect.html)
  * [日本語](/ja/current/Manual/class-AudioPitchShifterEffect.html)
  * [한국어](/kr/current/Manual/class-AudioPitchShifterEffect.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AudioPitchShifterEffect.html)
  * [中文](/cn/current/Manual/class-AudioPitchShifterEffect.html)
  * [日本語](/ja/current/Manual/class-AudioPitchShifterEffect.html)
  * [한국어](/kr/current/Manual/class-AudioPitchShifterEffect.html)

  * [Audio](Audio.html)
  * [Audio Reference](AudioReference.html)
  * [Audio Effects](class-AudioEffectMixer.html)
  * Audio Pitch Shifter Effect

[](class-AudioParamEQEffect.html)

Audio Parametric Equalizer Effect

[](class-AudioChorusEffect.html)

Audio Chorus Effect

# Audio Pitch Shifter Effect

The **Audio Pitch Shifter Effect** is used to shift a signal up or down in
pitch.

## Properties

![](../uploads/Main/AudioPitchShifterEffect.png) **_Property:_** | **_Function:_**  
---|---  
**Pitch** | The pitch multiplier (range 0.5 x to 2.0 x, default 1.0 x).  
**FFT Size** | The size of the FFT window used to analyze the audio signal during pitch shifting (range 256.0 to 4096.0, default = 1024.0). Higher values reduce smearing but require more processing power.  
**Overlap** | How much each successive FFT window overlaps (range 1 to 32, default = 4). Higher values mean smoother transitions, but increasing this property by a value of 2 doubles the CPU usage.  
**Max channels** | The maximum number of channels (range 0 to 16, default = 0 channels).  
  
AudioPitchShifterEffect

[](class-AudioParamEQEffect.html)

Audio Parametric Equalizer Effect

[](class-AudioChorusEffect.html)

Audio Chorus Effect

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

