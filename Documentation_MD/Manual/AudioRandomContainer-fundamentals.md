[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AudioRandomContainer-fundamentals.html)
  * [中文](/cn/current/Manual/AudioRandomContainer-fundamentals.html)
  * [日本語](/ja/current/Manual/AudioRandomContainer-fundamentals.html)
  * [한국어](/kr/current/Manual/AudioRandomContainer-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AudioRandomContainer-fundamentals.html)
  * [中文](/cn/current/Manual/AudioRandomContainer-fundamentals.html)
  * [日本語](/ja/current/Manual/AudioRandomContainer-fundamentals.html)
  * [한국어](/kr/current/Manual/AudioRandomContainer-fundamentals.html)

  * [Audio](Audio.html)
  * [Audio playlist randomization](AudioRandomContainer.html)
  * Audio Random Container fundamentals

[](AudioRandomContainer-UI.html)

Audio Random Container reference

[](Create-randomized-playlist.html)

Create a randomized playlist with the Audio Random Container

# Audio Random Container fundamentals

This page describes the audio concepts and terminology that you should
understand before you use the Audio Random Container to create a randomized
audio playlist.

The concepts you must know are the audio cycle and the AudioSource API
exceptions.

## Audio cycle

An audio cycle is the full audio clip list length. If the list has three audio
clips, an audio cycle is three clips.

### AudioSource API

Use the AudioSource APIs to start, pause, and stop an Audio Random Container.
This is similar to when you use the AudioSource APIs to play, pause, and stop
an Audio Clip, but with the following exceptions:

  * isPlaying returns true when the Audio Random Container plays an audio clip through an **audio source** A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource).

  * AudioSource.Play behaves differently depending on whether you set the Audio Random Container to Manual or Automatic. When set to Manual, the AudioSource.Play triggers a new instance in the Audio Clip list based on the Playback mode.

## Additional resources

Audio Clip, the audio cycle, the AudioSource priority, and the AudioSource API
exceptions.

  * [Audio Clips](class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip)

  * [Audio Source priority](class-AudioSource.html)
  * [Audio Mixer](AudioMixer.html)

[](AudioRandomContainer-UI.html)

Audio Random Container reference

[](Create-randomized-playlist.html)

Create a randomized playlist with the Audio Random Container

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

