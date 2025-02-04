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

# XRDisplaySubsystem

class in UnityEngine.XR

/

Inherits from:[IntegratedSubsystem](IntegratedSubsystem.html)

/

Implemented in:[UnityEngine.XRModule](UnityEngine.XRModule.html)

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

An XRDisplaySubsystem controls rendering to a head tracked display.

### Properties

[contentProtectionEnabled](XR.XRDisplaySubsystem-
contentProtectionEnabled.html)| Sets or gets the state of content protection
for the current active provider. For most providers, content protection allows
you to use write only textures for rendering. This stops the ability for apps
to read textures from the graphics card and view/record images that may be
protected in some way.  
---|---  
[disableLegacyRenderer](XR.XRDisplaySubsystem-disableLegacyRenderer.html)|
Disables the legacy renderer while this XRDisplaySubsystem is active.  
[displayOpaque](XR.XRDisplaySubsystem-displayOpaque.html)| Determines if the
current attached device has an opaque display. Most VR devices are opaque in
order to increase the immersive experience, AR devices are transparent to
allow for interaction with an augmentation of the current environment.  
[foveatedRenderingFlags](XR.XRDisplaySubsystem-foveatedRenderingFlags.html)|
Controls optional behavior of the foveated rendering system.  
[foveatedRenderingLevel](XR.XRDisplaySubsystem-foveatedRenderingLevel.html)|
Controls the intensity of the foveated rendering system.  
[hdrOutputSettings](XR.XRDisplaySubsystem-hdrOutputSettings.html)| The
HDROutputSettings for the XR Display Subsystem.  
[occlusionMaskScale](XR.XRDisplaySubsystem-occlusionMaskScale.html)| A scale
applied to the standard occulsion mask.  
[reprojectionMode](XR.XRDisplaySubsystem-reprojectionMode.html)| The kind of
reprojection the app requests to stabilize its holographic rendering relative
to the user's head motion.  
[scaleOfAllRenderTargets](XR.XRDisplaySubsystem-scaleOfAllRenderTargets.html)|
Controls the size of the textures submitted to the display as a multiplier of
the display's default resolution.  
[scaleOfAllViewports](XR.XRDisplaySubsystem-scaleOfAllViewports.html)|
Controls how much of the allocated display texture should be used for
rendering.  
[supportedTextureLayouts](XR.XRDisplaySubsystem-supportedTextureLayouts.html)|
Specifies all texture layouts supported by this display subsystem. This var is
a bit field that could be combination of XRDisplaySubsystem.TextureLayout.  
[textureLayout](XR.XRDisplaySubsystem-textureLayout.html)| Set
DisplaySubsystem to use certain texture layout. Should query supported texture
layout through XRDisplaySubsystem.supportedTextureLayouts first for the
capabilities.  
[zFar](XR.XRDisplaySubsystem-zFar.html)| Set DisplaySubsystem to use zFar for
rendering.  
[zNear](XR.XRDisplaySubsystem-zNear.html)| Set DisplaySubsystem to use zNear
for rendering.  
  
### Public Methods

[AddGraphicsThreadMirrorViewBlit](XR.XRDisplaySubsystem.AddGraphicsThreadMirrorViewBlit.html)|
This function records the display subsystem's native blit event to the target
command buffer. This function is typically called by a scriptable rendering
pipeline.  
---|---  
[BeginRecordingIfLateLatched](XR.XRDisplaySubsystem.BeginRecordingIfLateLatched.html)|
This function enables late latching recording of constant buffer memory
locations which are later patched with the latest pose data.  
[EndRecordingIfLateLatched](XR.XRDisplaySubsystem.EndRecordingIfLateLatched.html)|
This function disables late latching recording of constant buffer locations.  
[GetCullingParameters](XR.XRDisplaySubsystem.GetCullingParameters.html)| Gets
culling parameters for a specific culling pass index.  
[GetMirrorViewBlitDesc](XR.XRDisplaySubsystem.GetMirrorViewBlitDesc.html)| Get
a mirror view blit operation descriptor from the current display subsystem.  
[GetPreferredMirrorBlitMode](XR.XRDisplaySubsystem.GetPreferredMirrorBlitMode.html)|
Returns the XR display's preferred mirror blit mode.  
[GetRenderPass](XR.XRDisplaySubsystem.GetRenderPass.html)| Gets an
XRRenderPass of a specific index.  
[GetRenderPassCount](XR.XRDisplaySubsystem.GetRenderPassCount.html)| The
number of XRRenderPass entries for this XR Display.  
[GetRenderTexture](XR.XRDisplaySubsystem.GetRenderTexture.html)| Given the
UnityXRRenderTextureID returned by IUnityXRDisplayInterface::CreateTexture,
return the managed UnityEngine.RenderTexture instance.  
[GetRenderTextureForRenderPass](XR.XRDisplaySubsystem.GetRenderTextureForRenderPass.html)|
Given a render pass, return the RenderTexture instance backing that render
pass. If the render pass is invalid, or if the render texture does not exist,
return null.  
[GetSharedDepthTextureForRenderPass](XR.XRDisplaySubsystem.GetSharedDepthTextureForRenderPass.html)|
Given a render pass, return the shared depth buffer RenderTexture instance
backing that render pass. If the render pass is invalid, or if the render
texture does not exist, return null.  
[MarkTransformLateLatched](XR.XRDisplaySubsystem.MarkTransformLateLatched.html)|
This marks a given GameObject's transform to be late latched in the next
frame. Once marked for late latching, the GameObject transform and its
descendants will be updated with the latest VR pose updates before rendering
is submitted to the GPU.  
[SetFocusPlane](XR.XRDisplaySubsystem.SetFocusPlane.html)| Sets a point in 3D
space that acts as the focal point of the Scene for this frame. This helps to
improve the visual fidelity of content around this point. You must set this
value every frame. Note that specifying body-locked content in focus improves
the fidelity of body-locked content at the expense of content not locked to
the body. This is especially apparent when the user moves.  
[SetMSAALevel](XR.XRDisplaySubsystem.SetMSAALevel.html)| Set MSAA level for
the DisplaySubsystem's render texture.  
[SetPreferredMirrorBlitMode](XR.XRDisplaySubsystem.SetPreferredMirrorBlitMode.html)|
Override the XR display's preferred mirror blit mode from the script.  
[TryGetAppGPUTimeLastFrame](XR.XRDisplaySubsystem.TryGetAppGPUTimeLastFrame.html)|
Retrieves the time the GPU has spent on executing commands from the
application's last frame, as reported by the XR Plugin. Measured in seconds.  
[TryGetCompositorGPUTimeLastFrame](XR.XRDisplaySubsystem.TryGetCompositorGPUTimeLastFrame.html)|
Retrieves the amount of time that the GPU spent executing the compositor
renderer during the last frame, as reported by the XR Plugin. Measured in
seconds.  
[TryGetDisplayRefreshRate](XR.XRDisplaySubsystem.TryGetDisplayRefreshRate.html)|
Retrieves the refresh rate of the display as reported by the XR Plugin.  
[TryGetDroppedFrameCount](XR.XRDisplaySubsystem.TryGetDroppedFrameCount.html)|
Retrieves the number of dropped frames reported by the XR Plugin.  
[TryGetFramePresentCount](XR.XRDisplaySubsystem.TryGetFramePresentCount.html)|
Retrieves the number of times the current frame has been drawn to the device
as reported by the XR Plugin.  
[TryGetMotionToPhoton](XR.XRDisplaySubsystem.TryGetMotionToPhoton.html)|
Retrieves the motion-to-photon value as reported by the XR Plugin.  
  
### Events

[displayFocusChanged](XR.XRDisplaySubsystem-displayFocusChanged.html)| Event
sent when XR display focus changes.  
---|---  
  
### Inherited Members

### Properties

[running](IntegratedSubsystem-running.html)| Whether or not the subsystem is
running.  
---|---  
  
### Public Methods

[Destroy](IntegratedSubsystem.Destroy.html)| Destroys this instance of a
subsystem.  
---|---  
[Start](IntegratedSubsystem.Start.html)| Starts an instance of a subsystem.  
[Stop](IntegratedSubsystem.Stop.html)| Stops an instance of a subsystem.  
  
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

