[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AudioSource.html)
  * [中文](/cn/current/Manual/class-AudioSource.html)
  * [日本語](/ja/current/Manual/class-AudioSource.html)
  * [한국어](/kr/current/Manual/class-AudioSource.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AudioSource.html)
  * [中文](/cn/current/Manual/class-AudioSource.html)
  * [日本語](/ja/current/Manual/class-AudioSource.html)
  * [한국어](/kr/current/Manual/class-AudioSource.html)

  * [Audio](Audio.html)
  * [Audio Reference](AudioReference.html)
  * Audio Source

[](class-AudioListener.html)

Audio Listener

[](class-AudioMixer.html)

Audio Mixer

# Audio Source

[Switch to Scripting](../ScriptReference/AudioSource.html "Go to AudioSource
page in the Scripting Reference")

The **Audio Source** plays back an [Audio Clip](class-AudioClip.html) in the
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). The clip can be played to an [audio
listener](class-AudioListener.html) or through an [audio mixer](class-
AudioMixer.html). The audio source can play any type of [Audio Clip](class-
AudioClip.html) and can be configured to play these as 2D, 3D, or as a mixture
(_SpatialBlend_). The audio can be spread out between speakers (stereo to 7.1)
(_Spread_) and morphed between 3D and 2D (_SpatialBlend_). This can be
controlled over distance with falloff curves. Also, if the [listener](class-
AudioListener.html) is within one or multiple [Reverb Zones](class-
AudioReverbZone.html), reverberation is applied to the source. Individual
filters can be applied to each audio source for an even richer audio
experience. See [Audio Effects](class-AudioEffect.html)Any effect that can
modify the output of Audio Mixer components, such as filtering frequency
ranges of a sound or applying reverb. [More info](class-AudioEffectMixer.html)  
See in [Glossary](Glossary.html#AudioEffect) for more details.

![](../uploads/Main/AudioSourceInspector.png)

## Properties

**Property** | **Description**  
---|---  
**Audio Clip** A container for audio data in Unity. Unity supports mono,
stereo and multichannel audio assets (up to eight channels). Unity can import
.aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m
tracker module formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip) | Reference to the sound clip file that will be played.  
**Output** | By default, the clip is output directly to the [Audio Listener](class-AudioListener.html) in the Scene. Use this property to output the clip to an [Audio Mixer](class-AudioMixer.html) instead.  
**Mute** | If enabled the sound will be playing but muted.  
**Spatialize** | Enables or disables custom spatialization for the Audio Source. This property is only available if you have installed an [audio spatializer SDK](AudioSpatializerSDK.html), and selected it in your project’s global [audio](class-AudioManager.html) settings.  
**Spatialize Post Effect** | Determines whether the custom spatializer is applied before or after other effects attached to the Audio Source. Enable this property to apply the custom spatializer after other effects attached to the Audio Source. This property is only available if you have enabled the Spatialize property for the Audio Source.  
**Bypass Effects** | This is to quickly “by-pass” filter effects applied to the audio source. An easy way to turn all effects on/off.  
**Bypass Listener Effects** | This is to quickly turn all Listener effects on/off.  
**Bypass Reverb Zones** | This is to quickly turn all Reverb Zones on/off.  
**Play On Awake** Set this to true to make an Audio Source start playing on
awake [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#PlayOnAwake) | If enabled, the sound will start playing the moment the scene launches. If disabled, you need to start it using the **Play()** command from scripting.  
**Loop** | Enable this to make the **Audio Clip** loop when it reaches the end.  
**Priority** | Determines the priority of this audio source among all the ones that coexist in the scene. (Priority: 0 = most important. 256 = least important. Default = 128.). Use 0 for music tracks to avoid it getting occasionally swapped out.  
**Volume** | How loud the sound is at a distance of one world unit (one meter) from the **Audio Listener** A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](class-AudioListener.html)  
See in [Glossary](Glossary.html#AudioListener).  
**Pitch** | Amount of change in pitch due to slowdown/speed up of the **Audio Clip**. Value 1 is normal playback speed.  
**Stereo Pan** | Sets the position in the stereo field of 2D sounds.  
**Spatial Blend** | Sets how much the 3D engine has an effect on the audio source.  
**Reverb Zone Mix** | Sets the amount of the output signal that gets routed to the reverb zones. The amount is linear in the (0 - 1) range, but allows for a 10 dB amplification in the (1 - 1.1) range which can be useful to achieve the effect of near-field and distant sounds.  
****3D Sound Settings**** | Settings that are applied proportionally to the Spatial Blend parameter.  
**Doppler Level** | Determines how much doppler effect will be applied to this audio source (if is set to 0, then no effect is applied).  
**Spread** | Sets the spread angle to 3D stereo or multichannel sound in speaker space.  
**Min Distance** | Within the MinDistance, the sound will stay at loudest possible. Outside MinDistance it will begin to attenuate. Increase the MinDistance of a sound to make it ‘louder’ in a 3d world, and decrease it to make it ‘quieter’ in a 3d world.  
**Max Distance** | The distance where the sound stops attenuating at. Beyond this point it will stay at the volume it would be at MaxDistance units from the listener and will not attenuate any more.  
**Rolloff Mode** | How fast the sound fades. The higher the value, the closer the Listener has to be before hearing the sound. (This is determined by a Graph).  
**\- Logarithmic Rolloff** | The sound is loud when you are close to the audio source, but when you get away from the object it decreases significantly fast.  
**\- Linear Rolloff** | The further away from the audio source you go, the less you can hear it.  
**\- Custom Rolloff** | The sound from the audio source behaves accordingly to how you set the graph of roll offs.  
  
## Types of Rolloff

There are three Rolloff modes: Logarithmic, Linear and Custom Rolloff. The
Custom Rolloff can be modified by modifying the volume distance curve as
described below. If you try to modify the volume distance function when it is
set to Logarithmic or Linear, the type will automatically change to Custom
Rolloff.

![Rolloff Modes that an audio source can
have.](../uploads/Main/TypesOfRollOff.png) Rolloff Modes that an audio source
can have.

## Distance Functions

There are several properties of the audio that can be modified as a function
of the distance between the audio source and the audio listener.

**Volume** : Amplitude(0.0 - 1.0) over distance.

**Spatial Blend** : 2D (original channel mapping) to 3D (all channels
downmixed to mono and attenuated according to distance and direction).

**Spread** : Angle (degrees 0.0 - 360.0) over distance.

**Low-Pass** (only if LowPassFilter is attached to the AudioSource): Cutoff
Frequency (22000.0–10.0) over distance.

**Reverb Zone** : Amount of signal routed to the reverb zones. Note that the
volume property and distance and directional attenuation are applied to the
signal first and therefore affect both the direct and reverberated signals.

![Distance functions for Volume, Spatial Blend, Spread, Low-Pass audio filter,
and Reverb Zone Mix. The current distance to the Audio Listener is marked in
the graph by the red vertical
line.](../uploads/Main/AudioDistanceFunctions.png) Distance functions for
Volume, Spatial Blend, Spread, Low-Pass audio filter, and Reverb Zone Mix. The
current distance to the Audio Listener is marked in the graph by the red
vertical line.

To modify the distance functions, you can edit the curves directly. For more
information, see the guide to [Editing Curves](EditingCurves.html).

## Creating Audio Sources

Audio Sources don’t do anything without an assigned **Audio Clip**. The Clip
is the actual sound file that will be played back. The Source is like a
controller for starting and stopping playback of that clip, and modifying
other audio properties.

To create a new Audio Source:

  1. Import your audio files into your Unity Project. These are now Audio Clips.
  2. Create an Audio Source GameObject (menu: **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) > **Audio** > **Audio Source**).

  3. With the new GameObject selected, select **Component** A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](UsingComponents.html)  
See in [Glossary](Glossary.html#component) > **Audio** > **Audio Source**.

  4. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), find the **Audio Clip** property
on the Audio Source Component and assign a clip, either by dragging one from
the **Project Window** A window that shows the contents of your `Assets`
folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow) or by clicking the small circle
icon to the right of the Inspector property, then selecting a clip from the
list.

**Note:** If you want to create an **Audio Source** just for one **Audio
Clip** that you have in the Assets folder then you can just drag that clip to
the **scene view** An interactive view into the world you are creating. You
use the Scene View to select and position scenery, characters, cameras,
lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) \- a GameObject with an **Audio
Source** component will be created automatically for it. Dragging a clip onto
on existing GameObject will attach the clip along with a new **Audio Source**
if there isn’t one already there. If the object does already have an **Audio
Source** then the newly dragged clip will replace the one that the source
currently uses.

## API resources

  * [AudioSource](../ScriptReference/AudioSource.html)
  * [AudioClip](../ScriptReference/AudioClip.html)
  * [AudioListener](../ScriptReference/AudioListener.html)
  * [AudioMixer](../ScriptReference/Audio.AudioMixer.html)

AudioSource

[](class-AudioListener.html)

Audio Listener

[](class-AudioMixer.html)

Audio Mixer

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

