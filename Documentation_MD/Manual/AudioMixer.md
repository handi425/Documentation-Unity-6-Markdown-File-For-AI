[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AudioMixer.html)
  * [中文](/cn/current/Manual/AudioMixer.html)
  * [日本語](/ja/current/Manual/AudioMixer.html)
  * [한국어](/kr/current/Manual/AudioMixer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AudioMixer.html)
  * [中文](/cn/current/Manual/AudioMixer.html)
  * [日本語](/ja/current/Manual/AudioMixer.html)
  * [한국어](/kr/current/Manual/AudioMixer.html)

  * [Audio](Audio.html)
  * Audio Mixer

[](TrackerModules.html)

Tracker Modules

[](AudioMixerOverview.html)

An overview of the concepts and Audio Mixer

# Audio Mixer

The Unity Audio Mixer allows you to mix various audio sources, apply effects
to them, and perform mastering.

## Audio Mixer Window

The window displays the Audio Mixer which is basically a tree of Audio Mixer
Groups. An Audio Mixer group is essentially a mix of audio, a signal chain
which allows you to apply volume attenuation and pitch correction; it allows
you to insert effects that process the audio signal and change the parameters
of the effects. There is also a send and return mechanism to pass the results
from one bus to another.

![The Audio Mixer](../uploads/Main/AudioMixer1.png) The Audio Mixer

An Audio Mixer is an asset. You can create one or more Audio Mixer and have
more than one active at any time. An Audio Mixer always contains a master
group. Other groups can then be added to define the structure of the mixer.

**Note:** The Web platform only partially supports Audio Mixers. For more
information on how audio is used in the Web platform, refer to [Audio in
Web](webgl-audio.html).

### How it works

You route the output of an [Audio Source](class-AudioSource.html)A component
which plays back an Audio Clip in the scene to an audio listener or through an
audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) to a group within an Audio Mixer.
The effects will then be applied to that signal.

The output of an Audio Mixer can be routed into any other group in any other
Audio Mixer in a **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) enabling you to chain up a number of
Audio Mixers in a scene to produce complex routing, effect processing and
snapshot applying.

### Snapshots

You can capture the settings of all the parameters in a group as a snapshot.
If you create a list of snapshots you can then transition between them in
gameplay to create different moods or themes.

### Ducking

Ducking allows you to alter the effect of one group based on what is happening
in another group. An example might be to reduce the background ambient noise
while something else is happening.

### Views

Different views can be set up. You can disable the visibility of certain
groups within a mixer and set this as a view. You can then transition between
views as required.

[](TrackerModules.html)

Tracker Modules

[](AudioMixerOverview.html)

An overview of the concepts and Audio Mixer

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

