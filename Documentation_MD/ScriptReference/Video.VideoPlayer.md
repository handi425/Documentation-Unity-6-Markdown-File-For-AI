[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# VideoPlayer

class in UnityEngine.Video

/

Inherits from:[Behaviour](Behaviour.html)

/

Implemented in:[UnityEngine.VideoModule](UnityEngine.VideoModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Plays video content onto a target.

Content can be either a [VideoClip](Video.VideoClip.html) imported asset or a
URL such as `file://` or `http://`. Video content will be projected onto one
of the supported targets, such as camera background or
[RenderTexture](RenderTexture.html). If the video content includes
transparency, this transparency will be present in the target, allowing
objects behind the video target to be visible. When the data
[VideoPlayer.source](Video.VideoPlayer-source.html) is set to URL, the audio
and video description of what is being played will only be initialized once
the [VideoPlayer](Video.VideoPlayer.html) preparation is completed. You can
test this with [VideoPlayer.isPrepared](Video.VideoPlayer-isPrepared.html).  
  
Refer to [Video file compatibility](../Manual/VideoSources-
FileCompatibility.html) for more information on supported video file formats.  
  
**The following demonstrates a few features of the VideoPlayer:**

    
    
    // Examples of [VideoPlayer](Video.VideoPlayer.html) function  
      
    using UnityEngine;
    using UnityEngine.Video;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Will attach a [VideoPlayer](Video.VideoPlayer.html) to the main camera.
            [GameObject](GameObject.html) camera = [GameObject.Find](GameObject.Find.html)("Main [Camera](Camera.html)");  
      
            // [VideoPlayer](Video.VideoPlayer.html) automatically targets the camera backplane when it is added
            // to a camera object, no need to change videoPlayer.targetCamera.
            var videoPlayer = camera.AddComponent<UnityEngine.Video.VideoPlayer>();  
      
            // Play on awake defaults to true. Set it to false to avoid the url set
            // below to auto-start playback since we're in Start().
            videoPlayer.playOnAwake = false;  
      
            // By default, VideoPlayers added to a camera will use the far plane.
            // Let's target the near plane instead.
            videoPlayer.renderMode = UnityEngine.Video.VideoRenderMode.CameraNearPlane;  
      
            // This will cause our [Scene](SceneManagement.Scene.html) to be visible through the video being played.
            videoPlayer.targetCameraAlpha = 0.5F;  
      
            // Set the video to play. URL supports local absolute or relative paths.
            // Here, using absolute.
            videoPlayer.url = "/Users/graham/movie.mov";  
      
            // Skip the first 100 frames.
            videoPlayer.frame = 100;  
      
            // Restart from beginning when done.
            videoPlayer.isLooping = true;  
      
            // Each time we reach the end, we slow down the playback by a factor of 10.
            videoPlayer.loopPointReached += EndReached;  
      
            // Start playback. This means the [VideoPlayer](Video.VideoPlayer.html) may have to prepare (reserve
            // resources, pre-load a few frames, etc.). To better control the delays
            // associated with this preparation one can use videoPlayer.Prepare() along with
            // its prepareCompleted event.
            videoPlayer.Play();
        }  
      
        void EndReached(UnityEngine.Video.VideoPlayer vp)
        {
            vp.playbackSpeed = vp.playbackSpeed / 10.0F;
        }
    }
    

### Static Properties

[controlledAudioTrackMaxCount](Video.VideoPlayer-
controlledAudioTrackMaxCount.html)| Maximum number of audio tracks that can be
controlled. (Read Only)  
---|---  
  
### Properties

[aspectRatio](Video.VideoPlayer-aspectRatio.html)| Defines how the video
content will be stretched to fill the target area.  
---|---  
[audioOutputMode](Video.VideoPlayer-audioOutputMode.html)| Destination for the
audio embedded in the video.  
[audioTrackCount](Video.VideoPlayer-audioTrackCount.html)| Number of audio
tracks found in the data source currently configured. (Read Only)  
[canSetDirectAudioVolume](Video.VideoPlayer-canSetDirectAudioVolume.html)|
Whether direct-output volume controls are supported for the current platform
and video format. (Read Only)  
[canSetPlaybackSpeed](Video.VideoPlayer-canSetPlaybackSpeed.html)| Whether you
can change the playback speed. (Read Only)  
[canSetSkipOnDrop](Video.VideoPlayer-canSetSkipOnDrop.html)| Whether frame-
skipping to maintain synchronization can be controlled. (Read Only)  
[canSetTime](Video.VideoPlayer-canSetTime.html)| Whether you can change the
current time using the VideoPlayer.time or VideoPlayer.frame properties. (Read
Only)  
[canSetTimeUpdateMode](Video.VideoPlayer-canSetTimeUpdateMode.html)| Whether
you can change the time source followed by the VideoPlayer. (Read Only)  
[canStep](Video.VideoPlayer-canStep.html)| Returns true if the VideoPlayer can
step forward through the video content. (Read Only)  
[clip](Video.VideoPlayer-clip.html)| The clip being played by the VideoPlayer.  
[clockTime](Video.VideoPlayer-clockTime.html)| The clock time that the
VideoPlayer follows to schedule its samples. The clock time is expressed in
seconds. (Read Only)  
[controlledAudioTrackCount](Video.VideoPlayer-controlledAudioTrackCount.html)|
Number of audio tracks that this VideoPlayer will take control of.  
[externalReferenceTime](Video.VideoPlayer-externalReferenceTime.html)|
Reference time of the external clock the VideoPlayer uses to correct its
drift.  
[frame](Video.VideoPlayer-frame.html)| The frame index of the currently
available frame in VideoPlayer.texture.  
[frameCount](Video.VideoPlayer-frameCount.html)| Number of frames in the
current video content. (Read Only)  
[frameRate](Video.VideoPlayer-frameRate.html)| The frame rate of the clip or
URL in frames/second. (Read Only)  
[height](Video.VideoPlayer-height.html)| The height of the images in the
VideoClip, or URL, in pixels. (Read Only)  
[isLooping](Video.VideoPlayer-isLooping.html)| Determines whether the
VideoPlayer restarts from the beginning when it reaches the end of the clip.  
[isPaused](Video.VideoPlayer-isPaused.html)| Whether playback is paused. (Read
Only)  
[isPlaying](Video.VideoPlayer-isPlaying.html)| Returns whether the VideoPlayer
is currently playing the content.  
[isPrepared](Video.VideoPlayer-isPrepared.html)| Returns whether the
VideoPlayer has successfully prepared the content to be played.  
[length](Video.VideoPlayer-length.html)| The length of the VideoClip, or the
URL, in seconds. (Read Only)  
[pixelAspectRatioDenominator](Video.VideoPlayer-
pixelAspectRatioDenominator.html)| Denominator of the pixel aspect ratio
(num:den) for the VideoClip or the URL. (Read Only)  
[pixelAspectRatioNumerator](Video.VideoPlayer-pixelAspectRatioNumerator.html)|
Numerator of the pixel aspect ratio (num:den) for the VideoClip or the URL.
(Read Only)  
[playbackSpeed](Video.VideoPlayer-playbackSpeed.html)| Factor by which the
basic playback rate will be multiplied.  
[playOnAwake](Video.VideoPlayer-playOnAwake.html)| Whether the content will
start playing back as soon as the component awakes.  
[renderMode](Video.VideoPlayer-renderMode.html)| Where the video content will
be drawn.  
[sendFrameReadyEvents](Video.VideoPlayer-sendFrameReadyEvents.html)| Enables
the frameReady events.  
[skipOnDrop](Video.VideoPlayer-skipOnDrop.html)| Whether the VideoPlayer is
allowed to skip frames to catch up with current time.  
[source](Video.VideoPlayer-source.html)| The source that the VideoPlayer uses
for playback.  
[targetCamera](Video.VideoPlayer-targetCamera.html)|  Camera component to draw
to when VideoPlayer.renderMode is set to either VideoRenderMode.CameraFarPlane
or VideoRenderMode.CameraNearPlane.  
[targetCamera3DLayout](Video.VideoPlayer-targetCamera3DLayout.html)| Type of
3D content contained in the source video media.  
[targetCameraAlpha](Video.VideoPlayer-targetCameraAlpha.html)| Overall
transparency level of the target camera plane video.  
[targetMaterialProperty](Video.VideoPlayer-targetMaterialProperty.html)|
Material texture property which is targeted when VideoPlayer.renderMode is set
to Video.VideoTarget.MaterialOverride.  
[targetMaterialRenderer](Video.VideoPlayer-targetMaterialRenderer.html)|
Renderer which is targeted when VideoPlayer.renderMode is set to
Video.VideoTarget.MaterialOverride  
[targetTexture](Video.VideoPlayer-targetTexture.html)|  RenderTexture to draw
to when VideoPlayer.renderMode is set to Video.VideoTarget.RenderTexture.  
[texture](Video.VideoPlayer-texture.html)| Internal texture in which video
content is placed. (Read Only)  
[time](Video.VideoPlayer-time.html)| The presentation time of the currently
available frame in VideoPlayer.texture in seconds.  
[timeReference](Video.VideoPlayer-timeReference.html)| The clock that the
VideoPlayer observes to detect and correct drift.  
[timeUpdateMode](Video.VideoPlayer-timeUpdateMode.html)| The clock source used
by the VideoPlayer to derive its current time.  
[url](Video.VideoPlayer-url.html)| The file or HTTP URL that the VideoPlayer
reads content from.  
[waitForFirstFrame](Video.VideoPlayer-waitForFirstFrame.html)| Determines
whether the VideoPlayer will wait for the first frame to be loaded into the
texture before starting playback when VideoPlayer.playOnAwake is on.  
[width](Video.VideoPlayer-width.html)| The width of the images in the
VideoClip, or URL, in pixels. (Read Only)  
  
### Public Methods

[EnableAudioTrack](Video.VideoPlayer.EnableAudioTrack.html)| Enable/disable
audio track decoding. Only effective when the VideoPlayer is not currently
playing.  
---|---  
[GetAudioChannelCount](Video.VideoPlayer.GetAudioChannelCount.html)| The
number of audio channels in the specified audio track.  
[GetAudioLanguageCode](Video.VideoPlayer.GetAudioLanguageCode.html)| Returns
the language code, if any, for the specified track.  
[GetAudioSampleRate](Video.VideoPlayer.GetAudioSampleRate.html)| Gets the
audio track sampling rate in Hertz.  
[GetDirectAudioMute](Video.VideoPlayer.GetDirectAudioMute.html)| Gets the
direct-output audio mute status for the specified track.  
[GetDirectAudioVolume](Video.VideoPlayer.GetDirectAudioVolume.html)| Return
the direct-output volume for specified track.  
[GetTargetAudioSource](Video.VideoPlayer.GetTargetAudioSource.html)| Gets the
AudioSource that will receive audio samples for the specified track if
VideoPlayer.audioOutputMode is set to VideoAudioOutputMode.AudioSource.  
[IsAudioTrackEnabled](Video.VideoPlayer.IsAudioTrackEnabled.html)| Whether
decoding for the specified audio track is enabled. See
VideoPlayer.EnableAudioTrack for distinction with mute.  
[Pause](Video.VideoPlayer.Pause.html)| Pauses the playback and leaves the
current time intact.  
[Play](Video.VideoPlayer.Play.html)| Starts or resumes the playback of a
video.  
[Prepare](Video.VideoPlayer.Prepare.html)| Prepares the playback engine so
that it's ready for playback.  
[SetDirectAudioMute](Video.VideoPlayer.SetDirectAudioMute.html)| Set the
direct-output audio mute status for the specified track.  
[SetDirectAudioVolume](Video.VideoPlayer.SetDirectAudioVolume.html)| Set the
direct-output audio volume for the specified track.  
[SetTargetAudioSource](Video.VideoPlayer.SetTargetAudioSource.html)| Sets the
AudioSource that will receive audio samples for the specified track if this
audio target is selected with VideoPlayer.audioOutputMode.  
[StepForward](Video.VideoPlayer.StepForward.html)| Immediately advance the
current time by one frame.  
[Stop](Video.VideoPlayer.Stop.html)| Stops the playback and sets the current
time to 0.  
  
### Events

[clockResyncOccurred](Video.VideoPlayer-clockResyncOccurred.html)| Invoked
when the VideoPlayer clock is synced back to its VideoTimeReference.  
---|---  
[errorReceived](Video.VideoPlayer-errorReceived.html)| Errors such as HTTP
connection problems are reported through this callback.  
[frameDropped](Video.VideoPlayer-frameDropped.html)| [NOT YET IMPLEMENTED]
Invoked when the video decoder does not produce a frame as per the time source
during playback.  
[frameReady](Video.VideoPlayer-frameReady.html)| Invoked when a new frame is
ready.  
[loopPointReached](Video.VideoPlayer-loopPointReached.html)| Invoked when the
VideoPlayer reaches the end of the content to play.  
[prepareCompleted](Video.VideoPlayer-prepareCompleted.html)| Invoked when the
VideoPlayer preparation is complete.  
[seekCompleted](Video.VideoPlayer-seekCompleted.html)| Invoke after a seek
operation completes.  
[started](Video.VideoPlayer-started.html)| Invoked immediately after Play is
called.  
  
### Delegates

[ErrorEventHandler](Video.VideoPlayer.ErrorEventHandler.html)| Delegate type
for VideoPlayer events that contain an error message.  
---|---  
[EventHandler](Video.VideoPlayer.EventHandler.html)| Delegate type for all
parameterless events emitted by VideoPlayers.  
[FrameReadyEventHandler](Video.VideoPlayer.FrameReadyEventHandler.html)|
Delegate type for VideoPlayer events that carry a frame number.  
[TimeEventHandler](Video.VideoPlayer.TimeEventHandler.html)| Delegate type for
VideoPlayer events that carry a time position.  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

