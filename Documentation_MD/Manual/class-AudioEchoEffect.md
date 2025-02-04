[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AudioEchoEffect.html)
  * [中文](/cn/current/Manual/class-AudioEchoEffect.html)
  * [日本語](/ja/current/Manual/class-AudioEchoEffect.html)
  * [한국어](/kr/current/Manual/class-AudioEchoEffect.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AudioEchoEffect.html)
  * [中文](/cn/current/Manual/class-AudioEchoEffect.html)
  * [日本語](/ja/current/Manual/class-AudioEchoEffect.html)
  * [한국어](/kr/current/Manual/class-AudioEchoEffect.html)

  * [Audio](Audio.html)
  * [Audio Reference](AudioReference.html)
  * [Audio Effects](class-AudioEffectMixer.html)
  * Audio Echo Effect

[](class-AudioHighPassEffect.html)

Audio High Pass Effect

[](class-AudioFlangeEffect.html)

Audio Flange Effect

# Audio Echo Effect

The **Audio Echo Effect** repeats a sound after a given **Delay** ,
attenuating the repetitions based on the **Decay Ratio**.

## Properties

![](../uploads/Main/AudioEchoEffect.png) **_Property:_** | **_Function:_**  
---|---  
**Delay** | Echo delay in ms. 10 to 5000. Default = 500.  
**Decay** | Echo decay per delay. 0 to 100%. 100% = No decay, 0% = total decay (ie simple 1 line delay). Default = 50%.  
**Max channels** | Maximum number of supported channels from 0 to 16 (default = 0).  
**Drymix** | Volume of original signal to pass to output. 0 to 100%. Default = 100%.  
**Wetmix** | Volume of echo signal to pass to output. 0 to 100%. Default = 100%.  
  
## Details

The **Wetmix** value determines the amplitude of the filtered signal, where
the **Drymix** determines the amplitude of the unfiltered sound output.

Hard surfaces reflects the propagation of sound. For example a large canyon
can be made more convincing with the Audio Echo Filter.

AudioEchoEffect

[](class-AudioHighPassEffect.html)

Audio High Pass Effect

[](class-AudioFlangeEffect.html)

Audio Flange Effect

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

