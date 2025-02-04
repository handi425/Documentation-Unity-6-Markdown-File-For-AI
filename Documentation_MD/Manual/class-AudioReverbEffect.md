[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AudioReverbEffect.html)
  * [中文](/cn/current/Manual/class-AudioReverbEffect.html)
  * [日本語](/ja/current/Manual/class-AudioReverbEffect.html)
  * [한국어](/kr/current/Manual/class-AudioReverbEffect.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AudioReverbEffect.html)
  * [中文](/cn/current/Manual/class-AudioReverbEffect.html)
  * [日本語](/ja/current/Manual/class-AudioReverbEffect.html)
  * [한국어](/kr/current/Manual/class-AudioReverbEffect.html)

  * [Audio](Audio.html)
  * [Audio Reference](AudioReference.html)
  * [Audio Effects](class-AudioEffectMixer.html)
  * Audio SFX Reverb Effect

[](class-AudioCompressor.html)

Audio Compressor Effect

[](class-AudioLowPassSimpleEffect.html)

Audio Low Pass Simple Effect

# Audio SFX Reverb Effect

The **SFX Reverb Effect** takes the output of an [Audio Mixer](class-
AudioMixer.html) group and distorts it to create a custom reverb effect.

## Properties

![](../uploads/Main/AudioSFXReverbEffect.png) **_Property:_** | **_Function:_**  
---|---  
**Dry Level** An audio setting that allows you to set the mix level of
unprocessed signal in output in mB.  
See in [Glossary](Glossary.html#DryLevel) | Mix level of dry signal in output in mB. Ranges from –10000.0 to 0.0. Default is 0 mB.  
**Room** | Room effect level at low frequencies in mB. Ranges from –10000.0 to 0.0. Default is –10000.0 mB.  
**Room HF** | Room effect high-frequency level in mB. Ranges from –10000.0 to 0.0. Default is 0.0 mB.  
**Decay Time** | Reverberation decay time at low-frequencies in seconds. Ranges from 0.1 to 20.0. Default is 1.0.  
**Decay HF Ratio** | Decay HF Ratio : High-frequency to low-frequency decay time ratio. Ranges from 0.1 to 2.0. Default is 0.5.  
**Reflections** | Early reflections level relative to room effect in mB. Ranges from –10000.0 to 1000.0. Default is –10000.0 mB.  
**Reflect Delay** | Early reflections delay time relative to room effect in mB. Ranges from –10000.0 to 2000.0. Default is 0.02.  
**Reverb** | Late reverberation level relative to room effect in mB. Ranges from –10000.0 to 2000.0. Default is 0.0 mB.  
**Reverb Delay** | Late reverberation delay time relative to first reflection in seconds. Ranges from 0.0 to 0.1. Default is 0.04 s.  
**Diffusion** | Reverberation diffusion (echo density) in percent. Ranges from 0.0 to 100.0. Default is 100.0%.  
**Density** | Reverberation density (modal density) in percent. Ranges from 0.0 to 100.0. Default is 100.0%.  
**HFReference** | Reference high frequency in Hz. Ranges from 20.0 to 20000.0. Default is 5000.0 Hz.  
**Room LF** | Room effect low-frequency level in mB. Ranges from –10000.0 to 0.0. Default is 0.0 mB.  
**LFReference** | Reference low-frequency in Hz. Ranges from 20.0 to 1000.0. Default is 250.0 Hz.  
  
AudioReverbEffect

[](class-AudioCompressor.html)

Audio Compressor Effect

[](class-AudioLowPassSimpleEffect.html)

Audio Low Pass Simple Effect

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

