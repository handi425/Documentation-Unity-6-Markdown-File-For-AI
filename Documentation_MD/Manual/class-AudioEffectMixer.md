[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AudioEffectMixer.html)
  * [中文](/cn/current/Manual/class-AudioEffectMixer.html)
  * [日本語](/ja/current/Manual/class-AudioEffectMixer.html)
  * [한국어](/kr/current/Manual/class-AudioEffectMixer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AudioEffectMixer.html)
  * [中文](/cn/current/Manual/class-AudioEffectMixer.html)
  * [日本語](/ja/current/Manual/class-AudioEffectMixer.html)
  * [한국어](/kr/current/Manual/class-AudioEffectMixer.html)

  * [Audio](Audio.html)
  * [Audio Reference](AudioReference.html)
  * Audio Effects

[](class-AudioChorusFilter.html)

Audio Chorus Filter

[](class-AudioLowPassEffect.html)

Audio Low Pass Effect

# Audio Effects

You can modify the output of [Audio Mixer](class-AudioMixer.html) components
by applying **Audio Effects**. These can filter the frequency ranges of the
sound or apply reverb and other effects.

The effects are applied by adding effect components to the relevant section of
the Audio Mixer. The ordering of the components is important, since it
reflects the order in which the effects will be applied to the source audio.
For example, in the image below, the Music section of an Audio Mixer is
modified first by a Lowpass effect and then a compressor Effect, Flange Effect
and so on.

![](../uploads/Main/AudioMixer1.png)

To change the ordering of these and any other components, open a context menu
in the **inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) and select the _Move Up_ or _Move
Down_ commands. Enabling or disabling an effect component determines whether
it will be applied or not.

Though highly optimized, some filters are still CPU intensive. Audio CPU usage
can monitored in the [profiler](Profiler.html)A window that helps you to
optimize your game. It shows how much time is spent in the various areas of
your game. For example, it can report the percentage of time spent rendering,
animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) under the Audio Tab.

See the other pages in this section for further information about the specific
effect types available.

AudioEffectMixer

[](class-AudioChorusFilter.html)

Audio Chorus Filter

[](class-AudioLowPassEffect.html)

Audio Low Pass Effect

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

