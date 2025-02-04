[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AudioChorusFilter.html)
  * [中文](/cn/current/Manual/class-AudioChorusFilter.html)
  * [日本語](/ja/current/Manual/class-AudioChorusFilter.html)
  * [한국어](/kr/current/Manual/class-AudioChorusFilter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AudioChorusFilter.html)
  * [中文](/cn/current/Manual/class-AudioChorusFilter.html)
  * [日本語](/ja/current/Manual/class-AudioChorusFilter.html)
  * [한국어](/kr/current/Manual/class-AudioChorusFilter.html)

  * [Audio](Audio.html)
  * [Audio Reference](AudioReference.html)
  * [Audio Filters](class-AudioEffect.html)
  * Audio Chorus Filter

[](class-AudioReverbFilter.html)

Audio Reverb Filter

[](class-AudioEffectMixer.html)

Audio Effects

# Audio Chorus Filter

[Switch to Scripting](../ScriptReference/AudioChorusFilter.html "Go to
AudioChorusFilter page in the Scripting Reference")

The **Audio Chorus Filter** takes an [Audio Clip](class-AudioClip.html)A
container for audio data in Unity. Unity supports mono, stereo and
multichannel audio assets (up to eight channels). Unity can import .aif, .wav,
.mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module
formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip) and processes it creating a chorus
effect.

## Properties

![](../uploads/Main/AudioChorusFilter.png) **_Property:_** | **_Function:_**  
---|---  
**Dry Mix** An audio setting that allows you to set the volume of the original
signal to pass to output.  
See in [Glossary](Glossary.html#DryMix) | Volume of original signal to pass to output. 0.0 to 1.0. Default = 0.5.  
**Wet Mix 1** | Volume of 1st chorus tap. 0.0 to 1.0. Default = 0.5.  
**Wet Mix 2** | Volume of 2nd chorus tap. This tap is 90 degrees out of phase of the first tap. 0.0 to 1.0. Default = 0.5.  
**Wet Mix 3** | Volume of 3rd chorus tap. This tap is 90 degrees out of phase of the second tap. 0.0 to 1.0. Default = 0.5.  
**Delay** | The LFO’s delay in ms. 0.1 to 100.0. Default = 40.0 ms  
**Rate** | The LFO’s modulation rate in Hz. 0.0 to 20.0. Default = 0.8 Hz.  
**Depth** | Chorus modulation depth. 0.0 to 1.0. Default = 0.03.  
**Feed Back** | Chorus feedback. Controls how much of the wet signal gets fed back into the filter’s buffer. 0.0 to 1.0. Default = 0.0.  
  
## Details

The chorus effect modulates the original sound by a sinusoid low frequency
oscillator (LFO). The output sounds like there are multiple sources emitting
the same sound with slight variations - resembling a choir.

You can tweak the chorus filter to create a flanger effect by lowering the
feedback and decreasing the delay, as the flanger is a variant of the chorus.

Creating a simple, dry echo is done by setting **Rate** and **Depth** to 0 and
tweaking the mixes and **Delay**

AudioChorusFilter

[](class-AudioReverbFilter.html)

Audio Reverb Filter

[](class-AudioEffectMixer.html)

Audio Effects

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

