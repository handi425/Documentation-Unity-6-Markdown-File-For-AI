[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/webgl-audio.html)
  * [中文](/cn/current/Manual/webgl-audio.html)
  * [日本語](/ja/current/Manual/webgl-audio.html)
  * [한국어](/kr/current/Manual/webgl-audio.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/webgl-audio.html)
  * [中文](/cn/current/Manual/webgl-audio.html)
  * [日本語](/ja/current/Manual/webgl-audio.html)
  * [한국어](/kr/current/Manual/webgl-audio.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * Audio in Web

[](webgl-graphics.html)

Web graphics

[](webgl-video.html)

Video playback in Web

# Audio in Web

This page only provides information about audio capabilities in the Web
platform. To learn how to use audio in your Unity project, refer to [Audio
Overview](AudioOverview.html).

Because Unity uses [FMOD](https://www.fmod.com)Audio in Unity is built on top
of a middleware called FMOD. FMOD is integrated with the Unity engine for
creating and playing back interactive audio.  
See in [Glossary](Glossary.html#FMOD) to manage audio for platforms, the Web
platform supports limited audio functionality, which only includes the basic
features. FMOD relies on threads, which the **WebGL** A JavaScript API that
renders 2D and 3D graphics in a web browser. The Unity Web build option allows
Unity to publish content as JavaScript programs which use HTML5 technologies
and the WebGL rendering API to run Unity content in a web browser. [More
info](webgl.html)  
See in [Glossary](Glossary.html#WebGL) API doesn’t support. For this reason,
Unity uses an implementation based on the internal Web Audio API, which
enables the browser to handle audio playback and mixing.

**Note:** Google Chrome’s new Autoplay policy prevents autoplay of audio and
video under certain conditions. For example, while your game might be set to
autoplay some background music soon after the game loads, it won’t play
automatically unless you click or tap on the website. For more information on
how to enable or disable this policy, refer to Google Chrome’s documentation
on [Autoplay policy in Chrome](https://developer.chrome.com/blog/autoplay/).

## Supported classes

Unity Web supports the following API classes:

**Class** | **WebGL Support status**  
---|---  
**[AudioSource](../ScriptReference/AudioSource.html)** | WebGL supports some APIs. Refer to [AudioSource](../ScriptReference/AudioSource.html) for specific support details.  
**[AudioListener](../ScriptReference/AudioListener.html)** | All APIs supported.  
**[AudioClip](../ScriptReference/AudioClip.html)** | WebGL supports some APIs. Refer to AudioClip for specific support details.  
**[AudioMixer](../ScriptReference/Audio.AudioMixer.html)** | WebGL supports some APIs. Refer to Audio Mixer for specific support details.  
**[SystemInfo.supportsAudio](../ScriptReference/SystemInfo-supportsAudio.html)** | The browser provides audio support for WebGL. For this reason, `SystemInfo.supportsAudio` is always true.  
**[Microphone](../ScriptReference/Microphone.html)** | Not supported.  
  
## AudioSource

The [AudioSource](../ScriptReference/AudioSource.html) API supports basic
positional audio playback, including:

  * Pausing and resuming
  * Rolloff
  * Pitch setting
  * Doppler effect support

Unity WebGL supports the following AudioSource APIs:

**Settings** | **Description**  
---|---  
**[Clip](../ScriptReference/AudioSource-clip.html)** | Determines the **audio clip** A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip) that plays next.  
**[dopplerLevel](../ScriptReference/AudioSource-dopplerLevel.html)** | Sets the Doppler scale for the AudioSource.  
**[ignoreListenerPause](../ScriptReference/AudioSource-ignoreListenerPause.html)** | Allows AudioSource to ignore `AudioListener.pause` and continue to play audio.  
**[ignoreListenerVolume](../ScriptReference/AudioSource-ignoreListenerVolume.html)** | Ignores the end-user’s AudioSource volume.  
**[isPlaying](../ScriptReference/AudioSource-isPlaying.html)** | Returns true if the `AudioSource.clip` is playing.  
**[loop](../ScriptReference/AudioSource-loop.html)** | Allows the application to loop the `AudioSource.clip`.  
**[maxDistance](../ScriptReference/AudioSource-maxDistance.html)** | Sets the maximum distance at which the `AudioSource.clip` stops attenuating or becomes inaudible.  
**[minDistance](../ScriptReference/AudioSource-minDistance.html)** | Sets the minimum distance at which the AudioSource.clip no longer rises in volumes. The sound starts to attenuate beyond the minimum distance.  
**[mute](../ScriptReference/AudioSource-mute.html)** | Mutes the AudioSource.  
**[pitch](../ScriptReference/AudioSource-pitch.html)** | Sets the pitch of the `AudioSource.clip`. WebGL only supports positive pitch values.  
**[playOnAwake](../ScriptReference/AudioSource-playOnAwake.html)** | Plays the AudioSource on Awake.  
**[rolloffMode](../ScriptReference/AudioSource-rolloffMode.html)** | Sets the AudioSource attenuation over distance.  
**[time](../ScriptReference/AudioSource-time.html)** | Sets the playback position in seconds.  
**[timeSamples](../ScriptReference/AudioSource-timeSamples.html)** | Sets the playback position in Pulse-code modulation (PCM) samples.  
**[velocityUpdateMode](../ScriptReference/AudioSource-velocityUpdateMode.html)** | Sets whether the AudioSource updates in the fixed or dynamic update loop.  
**[volume](../ScriptReference/AudioSource-volume.html)** | Sets the volume of the AudioSource (0.0 to 1.0).  
**[Pause](../ScriptReference/AudioSource.Pause.html)** | Pauses the `AudioSource.clip`.  
**[Play](../ScriptReference/AudioSource.Play.html)** | Plays the `AudioSource.clip`.  
**[PlayDelayed](../ScriptReference/AudioSource.PlayDelayed.html)** | Plays the `AudioSource.clip` with a delay you specify in seconds.  
**[PlayOneShot](../ScriptReference/AudioSource.PlayOneShot.html)** | Plays an [AudioClip](../ScriptReference/AudioSource-clip.html) and scales the AudioSource volume by volumeScale.  
**[PlayScheduled](../ScriptReference/AudioSource.PlayScheduled.html)** | Plays the AudioSource at a time you specify.  
**[SetScheduledEndTime](../ScriptReference/AudioSource.SetScheduledEndTime.html)** | Sets a time that a scheduled `AudioSource.clip` ends.  
**[SetScheduledStartTime](../ScriptReference/AudioSource.SetScheduledStartTime.html)** | Sets the time that a scheduled `AudioSource.clip` starts.  
**[Stop](../ScriptReference/AudioSource.Stop.html)** | Stops playing the `AudioSource.clip`.  
**[UnPause](../ScriptReference/AudioSource.UnPause.html)** | Unpauses a paused `AudioSource.clip`.  
**[PlayClipAtPoint](../ScriptReference/AudioSource.PlayClipAtPoint.html)** | Plays an `AudioSource.clip` at a given position in the worldspace.  
  
## AudioClip

Unity WebGL imports [AudioClip](../ScriptReference/AudioClip.html) files in
the AAC Format, which is supported by most browsers. Unity WebGL supports the
following AudioClip APIs:

**Properties** | **Description**  
---|---  
**[length](../ScriptReference/AudioClip-length.html)** | The length of the AudioClip in seconds.  
**[loadState](../ScriptReference/AudioClip-loadState.html)** | Returns the current load state of the audio data associated with an AudioClip.  
**[samples](../ScriptReference/AudioClip-samples.html)** | The length of the AudioClip in samples.  
**[loadType](../ScriptReference/AudioClip-loadType.html)** | The load type of the clip. You can set the AudioClip load type in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).  
**Method** | **Description** | **Additional information**  
---|---|---  
**[AudioClip.Create](../ScriptReference/AudioClip.Create.html)** | Creates an AudioClip with a name and length you specify. | Unity WebGL partially supports `AudioClip.Create`. Browsers don’t support dynamic streaming, so to use `AudioClip.Create`, set the Stream to false.  
**[AudioClip.SetData](../ScriptReference/AudioClip.SetData.html)** | Sets sample data in an AudioSource.clip. | Unity WebGL partially supports `AudioClip.SetData`. You can use this method only on compressed audio files with **Load Type** set to **Decompress on Load**. Refer to Compressed audio.  
**[AudioClip.GetData](../ScriptReference/AudioClip.GetData.html)** | Retrieves an array with sample data from an AudioSource.clip. | Unity WebGL partially supports `AudioClip.GetData`. You can use this method only on compressed audio files with **Load Type** set to **Decompress on Load**. Refer to Compressed audio.  
  
**Note:** For audio clip support on Linux, make sure you’ve installed the
[ffmpeg](https://ffmpeg.org/) package.

## Audio Mixer

Unity Web supports some functionality of [Audio Mixer](AudioMixer.html)
assets.

You can do the following with Audio Mixers on Web:

  * Create an Audio Mixer asset.
  * Add AudioMixerGroups to the hierarchy.
  * Adjust the volume of each group. To expose or change the volume with scripting, use [AudioMixer.SetFloat](../ScriptReference/Audio.AudioMixer.SetFloat.html).

**Note** : Volume is the only property you can change on Web. Other properties
and sound effects aren’t supported.

## Compressed audio

To use compressed audio with WebGL in Unity, set the AudioClip
[loadType](../ScriptReference/AudioClip-loadType.html) to one of the following
options:

  * [CompressedInMemory](../ScriptReference/AudioClipLoadType.CompressedInMemory.html)
  * [DecompressOnLoad](../ScriptReference/AudioClipLoadType.DecompressOnLoad.html)

****Compression** A method of storing data that reduces the amount of storage
space it requires. See [Texture Compression](class-TextureImporterOverride),
[Animation Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) method** | **Description** | **Considerations**  
---|---|---  
**CompressedInMemory** | Use this to compress the audio on disk and have it remain compressed after it loads into your application memory. | Compressed audio can cause latency and is less precise when it comes to audio playback. However, compressed audio uses less memory in your application than decompressed audio. It’s best practice to use `CompressedInMemory` for audio that’s unaffected by precision for example, background music.  
**DecompressOnLoad** | Use this to compress the audio on disk, similar to CompressedInMemory, and decompress when it loads into your application memory. | Decompressed audio uses a significant amount of memory compared to compressed audio but has lower latency and more audio flexibility. Use `DecompressedOnLoad` for audio that’s affected by precision (for example, character dialog or sound effects).  
  
## Audio playback and browser security

For security reasons, browsers don’t allow audio playback until an end user
interacts with your application webpage via a mouse click, touch event, or key
press. Use a loading screen to allow the end user to interact with your
application and start audio playback before your main content begins.

[](webgl-graphics.html)

Web graphics

[](webgl-video.html)

Video playback in Web

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

