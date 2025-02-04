[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AudioFiles.html)
  * [中文](/cn/current/Manual/AudioFiles.html)
  * [日本語](/ja/current/Manual/AudioFiles.html)
  * [한국어](/kr/current/Manual/AudioFiles.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AudioFiles.html)
  * [中文](/cn/current/Manual/AudioFiles.html)
  * [日本語](/ja/current/Manual/AudioFiles.html)
  * [한국어](/kr/current/Manual/AudioFiles.html)

  * [Audio](Audio.html)
  * Audio files

[](AudioOverview.html)

Audio overview

[](TrackerModules.html)

Tracker Modules

# Audio files

As with Meshes or Textures, the workflow for **Audio File** assets is designed
to be smooth and trouble free. Unity can import almost every common file
format but there are a few details that are useful to be aware of when working
with Audio Files.

Since Unity 5.0 audio data is separated from the actual AudioClips. The
AudioClips merely refer to the files containing the audio data and there are
various combinations of options in the AudioClip importer that determine how
the clips are loaded at runtime. This means that you have great flexibility
for deciding which audio assets should be kept in memory at all times (because
you may not be able to predict how often or how fast they will be playing,
i.e. footsteps, weapons and impacts), while other assets may be loaded on
demand or gradually as the player progresses through the level (speech,
background music, ambience loops etc).

When audio is encoded in Unity the main options for how it is stored on disk
is either _PCM_ , _ADPCM_ or _Compressed_. Additionally there are a few
platform-specific formats, but they work in similar ways. Unity supports most
common formats for importing audio (see the list below) and will import an
audio file when it is added to the project. The default mode is _Compressed_ ,
where the audio data is compressed with either Vorbis/MP3 for standalone and
mobile platforms.

See the [AudioClip](class-AudioClip.html) documentation for an extensive
description of the **compression** A method of storing data that reduces the
amount of storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) formats and other options
available for encoding audio data.

Any Audio File imported into Unity is available from **scripts** A piece of
code that allows you to create your own Components, trigger game events,
modify Component properties over time and respond to user input in any way you
like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) as an **Audio Clip** A container for
audio data in Unity. Unity supports mono, stereo and multichannel audio assets
(up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file
format, and .xm, .mod, .it, and .s3m tracker module formats. [More
info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip) instance, which provides a way for
the game runtime of the audio system to access the encoded audio data. The
game may access meta-information about the audio data via the AudioClip even
before the actual audio data has been loaded. This is possible because the
import process has extracted various bits of information such as length,
channel count and sample rate from the encoded audio data and stored it in the
AudioClip. This can for instance be useful when creating automatic dialogue or
music sequencing systems, because the music engine can use the information
about the length to schedule music playback before actually loading the data.
It also helps reducing memory usage by only keeping the audio clips in memory
that are needed at a time.

## Supported formats

**_Format_** | **_Extensions_**  
---|---  
MPEG layer 3 | .mp3  
Ogg Vorbis | .ogg  
Microsoft Wave | .wav  
Free Lossless Audio Codec (FLAC) | .flac  
Audio Interchange File Format | .aiff / .aif  
Ultimate Soundtracker module | .mod  
Impulse Tracker module | .it  
Scream Tracker module | .s3m  
FastTracker 2 module | .xm  
  
See the [Audio Overview](AudioOverview.html) for more information on using
sound in Unity.

[](AudioOverview.html)

Audio overview

[](TrackerModules.html)

Tracker Modules

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

