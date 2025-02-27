[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AudioOverview.html)
  * [中文](/cn/current/Manual/AudioOverview.html)
  * [日本語](/ja/current/Manual/AudioOverview.html)
  * [한국어](/kr/current/Manual/AudioOverview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AudioOverview.html)
  * [中文](/cn/current/Manual/AudioOverview.html)
  * [日本語](/ja/current/Manual/AudioOverview.html)
  * [한국어](/kr/current/Manual/AudioOverview.html)

  * [Audio](Audio.html)
  * Audio overview

[](Audio.html)

Audio

[](AudioFiles.html)

Audio files

# Audio overview

A game would be incomplete without some kind of audio, be it background music
or sound effects. Unity’s audio system can import most standard audio file
formats, play sounds in 3D space, and apply optional effects such as echo and
filtering. Unity can also record audio from any available microphone on your
machine for use during gameplay or for storage and transmission.

## Basic theory

In real life, objects emit sounds that listeners hear. The way a sound is
perceived depends on many factors. A listener can tell roughly which direction
a sound is coming from and may also get some sense of its distance from its
loudness and quality. A fast-moving sound source (such as a falling bomb or a
passing police car) changes in pitch as it moves as a result of the Doppler
Effect. Surroundings also affect the way sound is reflected. A voice inside a
cave has an echo, but the same voice in the open air doesn’t.

![Audio Sources and Listener](../uploads/Main/AudioSourceListDiagram.png)
Audio Sources and Listener

To simulate the effects of position, Unity requires sounds to originate from
Audio Sources attached to objects. The sounds emitted are then picked up by an
Audio Listener attached to another object, most often the main **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). Unity can then simulate the effects
of a source’s distance and position from the listener object and play them to
you accordingly. You can also use the relative speed of the source and
listener objects to simulate the Doppler Effect for added realism.

Unity can’t calculate echoes purely from **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) geometry, but you can simulate them by
adding **Audio Filters** Any audio filter that distorts the sound from an
Audio Source or sounds reaching the Audio Listener. [More info](class-
AudioEffect.html)  
See in [Glossary](Glossary.html#AudioFilter) to objects. For example, you
could apply the Echo filter to a sound that is supposed to be coming from
inside a cave. In situations where objects can move in and out of a place with
a strong echo, you can add a Reverb Zone to the scene. For example, your game
might involve cars driving through a tunnel. If you place a reverb zone inside
the tunnel, the cars’ engine sounds start to echo as they enter. The echo
quiets as the cars emerge from the other side.

With the Unity Audio Mixer, you can mix various audio sources, apply effects
to them, and perform mastering.

## Working with audio assets

Unity can import audio files in **AIFF** , **WAV** , **MP3** , and **Ogg**
formats in the same way as other assets. Drag the files into the Project
panel. Import an audio file to create an **Audio Clip** A container for audio
data in Unity. Unity supports mono, stereo and multichannel audio assets (up
to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file
format, and .xm, .mod, .it, and .s3m tracker module formats. [More
info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip) that you can then drag to an Audio
Source or use from a script. The Audio Clip reference page has more details
about the import options available for audio files.

For music, Unity also supports tracker modules, which use short audio samples
as “instruments” that you can arrange to play tunes. You can import tracker
modules from **.xm** , **.mod** , **.it** , and **.s3m** files and use them
the same way you use other audio clips.

## Audio recording

Unity can access the computer’s microphones from a script and create Audio
Clips by direct recording. The Microphone class provides an API to find
available microphones, query their capabilities, and start and end a recording
session. The script reference page for
[Microphone](../ScriptReference/Microphone.html) has further information and
code samples for audio recording.

## Additional resources

  * [Audio Source](class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource)

  * [Audio Listener](class-AudioListener.html)A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](class-AudioListener.html)  
See in [Glossary](Glossary.html#AudioListener)

  * [Audio Mixer](class-AudioMixer.html)
  * The [audio effects](class-AudioEffect.html)Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](class-AudioEffectMixer.html)  
See in [Glossary](Glossary.html#AudioEffect)

  * [Reverb Zones](class-AudioReverbZone.html)

[](Audio.html)

Audio

[](AudioFiles.html)

Audio files

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

