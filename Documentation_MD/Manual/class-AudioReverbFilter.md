[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AudioReverbFilter.html)
  * [中文](/cn/current/Manual/class-AudioReverbFilter.html)
  * [日本語](/ja/current/Manual/class-AudioReverbFilter.html)
  * [한국어](/kr/current/Manual/class-AudioReverbFilter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AudioReverbFilter.html)
  * [中文](/cn/current/Manual/class-AudioReverbFilter.html)
  * [日本語](/ja/current/Manual/class-AudioReverbFilter.html)
  * [한국어](/kr/current/Manual/class-AudioReverbFilter.html)

  * [Audio](Audio.html)
  * [Audio Reference](AudioReference.html)
  * [Audio Filters](class-AudioEffect.html)
  * Audio Reverb Filter

[](class-AudioDistortionFilter.html)

Audio Distortion Filter

[](class-AudioChorusFilter.html)

Audio Chorus Filter

# Audio Reverb Filter

[Switch to Scripting](../ScriptReference/AudioReverbFilter.html "Go to
AudioReverbFilter page in the Scripting Reference")

The **Audio Reverb Filter** takes an [Audio Clip](class-AudioClip.html)A
container for audio data in Unity. Unity supports mono, stereo and
multichannel audio assets (up to eight channels). Unity can import .aif, .wav,
.mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module
formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip) and distorts it to create a custom
reverb effect.

## Properties

![](../uploads/Main/AudioReverbFilter.png) **_Property:_** | **_Function:_**  
---|---  
**Reverb Preset** | Custom reverb presets, select user to create your own customized reverbs.  
**Dry Level** An audio setting that allows you to set the mix level of
unprocessed signal in output in mB.  
See in [Glossary](Glossary.html#DryLevel) | Mix level of dry signal in output in mB. Ranges from –10000.0 to 0.0. Default is 0.  
**Room** | Room effect level at low frequencies in mB. Ranges from –10000.0 to 0.0. Default is 0.0.  
**Room HF** | Room effect high-frequency level in mB. Ranges from –10000.0 to 0.0. Default is 0.0.  
**Room LF** | Room effect low-frequency level in mB. Ranges from –10000.0 to 0.0. Default is 0.0.  
**Decay Time** | Reverberation decay time at low-frequencies in seconds. Ranges from 0.1 to 20.0. Default is 1.0.  
**Decay HFRatio** | Decay HF Ratio : High-frequency to low-frequency decay time ratio. Ranges from 0.1 to 2.0. Default is 0.5.  
**Reflections Level** | Early reflections level relative to room effect in mB. Ranges from –10000.0 to 1000.0. Default is –10000.0.  
**Reflections Delay** | Early reflections delay time relative to room effect in mB. Ranges from 0 to 0.3. Default is 0.0.  
**Reverb Level** | Late reverberation level relative to room effect in mB. Ranges from –10000.0 to 2000.0. Default is 0.0.  
**Reverb Delay** | Late reverberation delay time relative to first reflection in seconds. Ranges from 0.0 to 0.1. Default is 0.04.  
**HFReference** | Reference high frequency in Hz. Ranges from 1000.0 to 20000.0. Default is 5000.0.  
**LFReference** | Reference low-frequency in Hz. Ranges from 20.0 to 1000.0. Default is 250.0.  
**Diffusion** | Reverberation diffusion (echo density) in percent. Ranges from 0.0 to 100.0. Default is 100.0.  
**Density** | Reverberation density (modal density) in percent. Ranges from 0.0 to 100.0. Default is 100.0.  
  
**Note:** These values can only be modified if your **Reverb Preset** is set
to **User** , else these values will be grayed out and they will have default
values for each preset.

AudioReverbFilter

[](class-AudioDistortionFilter.html)

Audio Distortion Filter

[](class-AudioChorusFilter.html)

Audio Chorus Filter

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

