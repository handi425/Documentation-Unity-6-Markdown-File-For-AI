[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-VideoPlayer.html)
  * [中文](/cn/current/Manual/class-VideoPlayer.html)
  * [日本語](/ja/current/Manual/class-VideoPlayer.html)
  * [한국어](/kr/current/Manual/class-VideoPlayer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-VideoPlayer.html)
  * [中文](/cn/current/Manual/class-VideoPlayer.html)
  * [日本語](/ja/current/Manual/class-VideoPlayer.html)
  * [한국어](/kr/current/Manual/class-VideoPlayer.html)

  * [Video and cutscenes](Video.html)
  * [Video Player](VideoPlayer.html)
  * Video Player component

[](VideoPlayer.html)

Video Player

[](VideoPlayer-MigratingFromMovieTexture.html)

Migrating from MovieTexture to VideoPlayer

# Video Player component

Use the Video Player [component](Components.html)A functional part of a
GameObject. A GameObject can contain any number of components. Unity has many
built-in components, and you can create your own by writing scripts that
inherit from MonoBehaviour. [More info](UsingComponents.html)  
See in [Glossary](Glossary.html#component) to attach [video files](Video.html)
to [GameObjects](GameObjects.html)The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), and play them on the GameObject’s
[Texture](Textures.html)An image used when rendering a GameObject, Sprite, or
UI element. Textures are often applied to the surface of a mesh to give it
visual detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture) at run time.

The screenshot below shows a Video Player component attached to a spherical
GameObject.

By default, the **Material Property** of a Video Player component is set to a
GameObject’s main texture, which means that when the Video Player component is
attached to a GameObject that has a Renderer, it automatically assigns itself
to the Texture on that Renderer (because this is the main Texture for the
GameObject). Here, the GameObject has a **Mesh** The main graphics primitive
of Unity. Meshes make up a large part of your 3D worlds. Unity supports
triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces
must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer component, so the Video Player
automatically assigns it to the Renderer field, which means the Video Clip
plays on the **Mesh Renderer** A mesh component that takes the geometry from
the Mesh Filter and renders it at the position defined by the object’s
Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer)’s Texture.

![A Video Player component attached to a spherical GameObject, playing the
Video Clip on the GameObject’s main Texture \(in this case, the Texture of the
Mesh Renderer\)](../uploads/Main/Video-1.png) A Video Player component
attached to a spherical GameObject, playing the Video Clip on the GameObject’s
main Texture (in this case, the Texture of the Mesh Renderer)

You can also set a specific target for the video to play on, including:

  * A [Camera](class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) plane

  * A [Render Texture](class-RenderTexture.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture)

  * A [Material](Materials.html)An asset that defines how a surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material) Texture parameter

  * Any [Texture](class-TextureImporter.html) field in a component

## Video Player component reference

**Property** | **Description**  
---|---  
**Source** | Choose the source type of your video.  
**Video Clip** | Select the [Video Clip](class-VideoClip.html) to assign to the Video Player component. This isn’t supported on the Web platform.  
**URL** | Enter the URL (for example, http:// or file://) of the video you want to assign to the Video Player.  
**Update Mode** | Set the clock source that the Video Player component uses to update its timing.  
| **DSP Time** | Use the same clock source that processes audio.  
| **Game Time** | Use the same clock source as the game clock. This clock source is affected by the [time scaling and capture frame rate settings](managing-time-and-frame-rate.html).  
| **Unscaled Game Time** | Use the same clock source as the game clock but without being affected by [time scaling or capture frame rate](managing-time-and-frame-rate.html).  
****Play On Awake** Set this to true to make an Audio Source start playing on
awake [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#PlayOnAwake)** | Play the video when the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) launches. Clear it if you want to
trigger the video playback at another point during runtime. Trigger it via
scripting with the `Play()` command.  
**Wait For First Frame** | Wait for the first frame of the source video to be ready for display before the game starts. Clear it to keep the video time in sync with the rest of the game, which might cause the first few frames to be discarded.  
**Loop** | Loop the source video when it reaches its end. Clear it to stop playing the video when it reaches the end.  
**Skip On Drop** | When you enable this option, and the Video Player component detects drift between the playback position and the game clock, the Video Player skips ahead. When you disable this option, the Video Player doesn’t correct for drift and systematically plays all frames.  
**Playback Speed** | Set a multiplier for the playback speed, as a value between 0 and 10. This is set to 1 (normal speed) by default. If the field is set to 2, the video plays at two times its normal speed.  
**Render Mode** | Choose how the video will render.  
| **Camera Far Plane** | Render the video on the Camera’s [far plane](class-Camera.html).  
| **Camera Near Plane** | Render the video on the Camera’s [near plane](class-Camera.html).  
| **Render Texture** | Render the video into a [Render Texture](class-RenderTexture.html).  
| **Material Override** | Render the video into a selected Texture property of a GameObject through its Renderer’s [Material](../ScriptReference/Material.html).  
| **API Only** | Render the video into the [VideoPlayer.texture](../ScriptReference/Video.VideoPlayer-texture.html) Scripting API property. You must use scripting to assign the Texture to its intended destination.  
**Camera** | Define the [Camera](class-Camera.html) receiving the video.  
**Alpha** | Set the global transparency level to add to the source video. This allows elements behind the plane to be visible through it. For more information about alpha channels, refer to [video transparency support](VideoTransparency.html).  
**3D Layout** | Choose the layout of 3D content in the source video.  
| **None** | Video doesn’t have any 3D content.  
| **Side by Side** | Video has 3D content where the left eye occupies the left half and right eye occupies the right half of video frames.  
| **Over Under** | Video has 3D content where the left eye occupies the upper half and right eye occupies the lower half of video frames.  
**Target Texture** | Define the Render Texture where the Video Player component renders its images.  
****Aspect Ratio** The relationship of an image’s proportional dimensions,
such as its width and height.  
See in [Glossary](Glossary.html#AspectRatio)** | Set the aspect ratio of the images that fill the **Camera Near Plane** , **Camera Far Plane** , or **Render Texture** when the corresponding **Render Mode** is used.  
| **No Scaling** | No scaling is used. The video is centered on the destination rectangle.  
| **Fit Vertically** | Scale the source to fit the destination rectangle vertically, cropping the left and right sides or leaving black areas on each side if necessary. The source aspect ratio is preserved.  
| **Fit Horizontally** | Scale the source to fit the destination rectangle horizontally, cropping the top and bottom regions or leaving black areas above and below if needed. The source aspect ratio is preserved.  
| **Fit Inside** | Scale the source to fit the destination rectangle without having to crop. Leaves black areas on the left and right or above and below as needed. The source aspect ratio is preserved.  
| **Fit Outside** | Scale the source to fit the destination rectangle without leaving black areas on the left and right or above and below, cropping as required. The source aspect ratio is preserved.  
| **Stretch** | Scale both horizontally or vertically to fit the destination rectangle. The source aspect ratio isn’t preserved.  
**Renderer** | Select the [Renderer](../ScriptReference/Renderer.html) where the Video Player component renders its images. When set to **None** , the **Renderer** on the same GameObject as the Video Player component is used.  
**Auto-Select Property** | When you enable this option, the Video Player component selects the [Renderer](../ScriptReference/Renderer.html)’s main texture automatically. When you disable this option, you can set the **Material Property** option manually.  
| **Material Property** | The name of the [Material Texture property](../ScriptReference/Material.SetTexture.html) that receives the Video Player component images.  
**Audio Output Mode** | Define how the source’s audio tracks are output.  
| **None** | Audio isn’t played.  
| **Audio Source** | Audio samples are sent to selected [audio sources](class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource), enabling Unity’s audio
processing to be applied.  
| **Direct** | Audio samples are sent directly to the audio output hardware, bypassing Unity’s audio processing.  
| **API Only (Experimental)** | Audio samples are sent to the associated [AudioSampleProvider](../ScriptReference/Experimental.Audio.AudioSampleProvider.html).  
**Controlled Tracks** | The number of audio tracks in the video.  
  
Only shown when **Source** is **URL**. When **Source** is **Video Clip** , the
number of tracks is determined by examining the video file.  
**Track Number** | Enable the associated audio track to use for playback. This must be set prior to playback.  
  
The text to the left of the checkbox provides information about the audio
track, specifically the track number, language, and number of channels.  
  
When the source is a URL, this information is only available during playback.  
  
This property only appears if your source is a Video Clip that has an audio
track (or tracks), or your source is a URL (allowing you to indicate how many
tracks are expected from the URL during playback).  
| **Audio Source** | The [audio source](class-AudioSource.html) through which the audio track is played. The targeted audio source can also play Audio Clips.  
  
The audio source’s playback controls (`Play On Awake` and `Play()` in
scripting API) don’t apply to the video source’s audio track.  
  
This property only appears when the **Audio Output Mode** is set to **Audio
Source**.  
| **Mute** | Mute the associated audio track. In **Audio Source** mode, the audio source’s control is used.  
  
This property only appears when the **Audio Output Mode** is set to
**Direct**.  
| **Volume** | Volume of the associated audio track. In **Audio Source** mode, the audio source’s volume is used.  
  
This property only appears when the **Audio Output Mode** is set to
**Direct**.  
  
## Video Player Scripting Example

The following script demonstrates a few of the Video Player component’s
features.

    
    
    // Examples of Video Player function
    
    using UnityEngine;
    
    public class Example : MonoBehaviour
    {
        void Start()
        {
            // Will attach a Video Player to the main camera.
            GameObject camera = GameObject.Find("Main Camera");
    
            // VideoPlayer automatically targets the camera backplane when it is added
            // to a camera object, no need to change videoPlayer.targetCamera.
            var videoPlayer = camera.AddComponent<UnityEngine.Video.VideoPlayer>();
    
            // Play on awake defaults to true. Set it to false to avoid the url set
            // below to auto-start playback since we're in Start().
            videoPlayer.playOnAwake = false;
    
            // By default, Video Players added to a camera will use the far plane.
            // Let's target the near plane instead.
            videoPlayer.renderMode = UnityEngine.Video.VideoRenderMode.CameraNearPlane;
    
            // This will cause our Scene to be visible through the video being played.
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
    
            // Start playback. This means the Video Player may have to prepare (reserve
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
    

VideoPlayer

[](VideoPlayer.html)

Video Player

[](VideoPlayer-MigratingFromMovieTexture.html)

Migrating from MovieTexture to VideoPlayer

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

