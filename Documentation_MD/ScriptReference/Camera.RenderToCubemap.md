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

#  [Camera](Camera.html).RenderToCubemap

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

## Declaration

public bool RenderToCubemap([Cubemap](Cubemap.html) cubemap, int faceMask);

### Parameters

cubemap | The cube map to render to.  
---|---  
faceMask | A bitmask which determines which of the six faces are rendered to.  
  
### Returns

**bool** False if rendering fails, else true.

### Description

Render into a static cubemap from this camera.

This function is mostly useful in the editor for "baking" static cubemaps of
your Scene. See wizard example below. If you want a real-time-updated cubemap,
use RenderToCubemap variant that uses a RenderTexture with a cubemap
dimension, see below.  
  
Camera's position, clear flags and clipping plane distances will be used to
render into cubemap faces. `faceMask` is a bitfield indicating which cubemap
faces should be rendered into. Each bit that is set corresponds to a face. Bit
numbers are integer values of [CubemapFace](CubemapFace.html) enum. By default
all six cubemap faces will be rendered (default value 63 has six lowest bits
on).  
  
This function will return `false` if rendering to cubemap fails. Some graphics
hardware does not support the functionality.  
  
Note also that ReflectionProbes are a more advanced way of performing real-
time reflections. Cubemaps can be created in the editor by selecting the
Create->Legacy option.  
  
Additional resources: [Cubemap assets](../Manual/class-Cubemap.html),
[Reflective shaders](../Manual/shader-ReflectiveFamily.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections;  
      
    public class RenderCubemapWizard : [ScriptableWizard](ScriptableWizard.html)
    {
        public [Transform](Transform.html) renderFromPosition;
        public [Cubemap](Cubemap.html) cubemap;  
      
        void OnWizardUpdate()
        {
            string helpString = "Select transform to render from and cubemap to render into";
            bool isValid = (renderFromPosition != null) && (cubemap != null);
        }  
      
        void OnWizardCreate()
        {
            // create temporary camera for rendering
            [GameObject](GameObject.html) go = new [GameObject](GameObject.html)("CubemapCamera");
            go.AddComponent<[Camera](Camera.html)>();
            // place it on the object
            go.transform.position = renderFromPosition.position;
            go.transform.rotation = [Quaternion.identity](Quaternion-identity.html);
            // render into cubemap
            go.GetComponent<[Camera](Camera.html)>().RenderToCubemap(cubemap);  
      
            // destroy temporary camera
            DestroyImmediate(go);
        }  
      
        [[MenuItem](MenuItem.html)("[GameObject](GameObject.html)/Render into [Cubemap](Cubemap.html)")]
        static void RenderCubemap()
        {
            [ScriptableWizard.DisplayWizard](ScriptableWizard.DisplayWizard.html)<RenderCubemapWizard>(
                "Render cubemap", "Render!");
        }
    }
    

* * *

## Declaration

public bool RenderToCubemap([RenderTexture](RenderTexture.html) cubemap, int
faceMask);

### Parameters

faceMask | A bitfield indicating which cubemap faces should be rendered into.  
---|---  
cubemap | The texture to render to.  
  
### Returns

**bool** False if rendering fails, else true.

### Description

Render into a cubemap from this camera.

This is used for real-time reflections into cubemap render textures. It can be
quite expensive though, especially if all six cubemap faces are rendered each
frame.  
  
The Camera's position, clear flags and clipping plane distances will be used
to render into cubemap faces. `faceMask` is a bitfield indicating which
cubemap faces should be rendered into. Each bit that is set corresponds to a
face. Bit numbers are integer values of [CubemapFace](CubemapFace.html) enum.
By default all six cubemap faces will be rendered (default value 63 has six
lowest bits on).  
  
This function will return `false` if rendering to cubemap fails. Some graphics
hardware does not support the functionality.  
  
Note that the RenderTexture must have [RenderTexture.dimension](RenderTexture-
dimension.html) set to
[TextureDimension.Cube](Rendering.TextureDimension.Cube.html). This is
illustrated in the example following.  
  
Additional resources: RenderTexture.isCubemap, [Reflective
shaders](../Manual/shader-ReflectiveFamily.html).

    
    
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Attach this script to an object that uses a Reflective shader.
        // Real-time reflective cubemaps!  
      
        int cubemapSize = 128;
        bool oneFacePerFrame = false;
        [Camera](Camera.html) cam;
        [RenderTexture](RenderTexture.html) renderTexture;  
      
    
        void Start()
        {
            // render all six faces at startup
            UpdateCubemap(63);
        }  
      
        void OnDisable()
        {
            DestroyImmediate(cam);
            DestroyImmediate(renderTexture);
        }  
      
        void LateUpdate()
        {
            if (oneFacePerFrame)
            {
                var faceToRender = [Time.frameCount](Time-frameCount.html) % 6;
                var faceMask = 1 << faceToRender;
                UpdateCubemap(faceMask);
            }
            else
            {
                UpdateCubemap(63); // all six faces
            }
        }  
      
        void UpdateCubemap(int faceMask)
        {
            if (!cam)
            {
                [GameObject](GameObject.html) obj = new [GameObject](GameObject.html)("CubemapCamera", typeof([Camera](Camera.html)));
                obj.hideFlags = [HideFlags.HideAndDontSave](HideFlags.HideAndDontSave.html);
                obj.transform.position = transform.position;
                obj.transform.rotation = [Quaternion.identity](Quaternion-identity.html);
                cam = obj.GetComponent<[Camera](Camera.html)>();
                cam.farClipPlane = 100; // don't render very far into cubemap
                cam.enabled = false;
            }  
      
            if (!renderTexture)
            {
                renderTexture = new [RenderTexture](RenderTexture.html)(cubemapSize, cubemapSize, 16);
                renderTexture.dimension = UnityEngine.Rendering.TextureDimension.Cube;
                renderTexture.hideFlags = [HideFlags.HideAndDontSave](HideFlags.HideAndDontSave.html);
                GetComponent<[Renderer](Renderer.html)>().sharedMaterial.SetTexture("_Cube", renderTexture);
            }  
      
            cam.transform.position = transform.position;
            cam.RenderToCubemap(renderTexture, faceMask);
        }
    }
    

* * *

## Declaration

public bool RenderToCubemap([RenderTexture](RenderTexture.html) cubemap, int
faceMask, [Camera.MonoOrStereoscopicEye](Camera.MonoOrStereoscopicEye.html)
stereoEye);

### Parameters

cubemap | The texture to render to.  
---|---  
faceMask | A bitfield indicating which cubemap faces should be rendered into. Set to the integer value 63 to render all faces.  
stereoEye | A Camera eye corresponding to the left or right eye for stereoscopic rendering, or neither for non-stereoscopic rendering.  
  
### Returns

**bool** False if rendering fails, else true.

### Description

Render one side of a stereoscopic 360-degree image into a cubemap from this
camera.

Setting the `stereoEye` parameter to
[Camera.MonoOrStereoscopicEye.Left](Camera.MonoOrStereoscopicEye.Left.html) or
[Camera.MonoOrStereoscopicEye.Right](Camera.MonoOrStereoscopicEye.Right.html)
renders the left or right eye point-of-view of a stereo 360 image with proper
world space transform. Setting `stereoEye` to
[Camera.MonoOrStereoscopicEye.Mono](Camera.MonoOrStereoscopicEye.Mono.html)
renders a monoscopic view of the Scene. After rendering the separate left and
right cubemaps, you can convert them into equirectangular panoramic images
that occupy one texture.  
  
When rendering either side of a stereoscopic view, the camera uses its
[stereoSeparation](Camera-stereoSeparation.html) value as the inter-pupillary
distance (IPD), unless VR Support is enabled. When using a VR camera, the VR
device IPD overrides the [stereoSeparation](Camera-stereoSeparation.html)
value.  
  
Unity uses the Camera's position, clear flags and clipping plane distances to
render into the cubemap faces. The camera is rotated for each face. `faceMask`
is a bitfield indicating which cubemap faces should be rendered into. Each bit
that is set corresponds to a face. Bit numbers are integer values of
[CubemapFace](CubemapFace.html) enum. For 360 stereo image capture, all six
cubemap faces should be rendered (set `facemask` to 63).  
  
This function will return `false` if rendering to the cubemap fails. Some
graphics hardware does not support the functionality.  
  
Note that the RenderTexture must have [RenderTexture.dimension](RenderTexture-
dimension.html) set to
[TextureDimension.Cube](Rendering.TextureDimension.Cube.html).  
  
Additional resources: RenderTexture.isCubemap, [Cubemap](../Manual/class-
Cubemap.html).

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    //attach this script to your camera object
    public class CreateStereoCubemaps : [MonoBehaviour](MonoBehaviour.html)
    {
        public [RenderTexture](RenderTexture.html) cubemapLeftEye;
        public [RenderTexture](RenderTexture.html) cubemapRightEye;
        public [RenderTexture](RenderTexture.html) equirect;
        public bool renderStereo = true;
        public float stereoSeparation = 0.064f;  
      
        void Start()
        {
            cubemapLeftEye = new [RenderTexture](RenderTexture.html)(1024, 1024, 24, [RenderTextureFormat.ARGB32](RenderTextureFormat.ARGB32.html));
            cubemapLeftEye.dimension = [TextureDimension.Cube](Rendering.TextureDimension.Cube.html);
            cubemapRightEye = new [RenderTexture](RenderTexture.html)(1024, 1024, 24, [RenderTextureFormat.ARGB32](RenderTextureFormat.ARGB32.html));
            cubemapRightEye.dimension = [TextureDimension.Cube](Rendering.TextureDimension.Cube.html);
            //equirect height should be twice the height of cubemap
            equirect = new [RenderTexture](RenderTexture.html)(1024, 2048, 24, [RenderTextureFormat.ARGB32](RenderTextureFormat.ARGB32.html));
        }  
      
        void LateUpdate()
        {
            [Camera](Camera.html) cam = GetComponent<[Camera](Camera.html)>();  
      
            if (cam == null)
            {
                cam = GetComponentInParent<[Camera](Camera.html)>();
            }  
      
            if (cam == null)
            {
                [Debug.Log](Debug.Log.html)("stereo 360 capture node has no camera or parent camera");
            }  
      
            if (renderStereo)
            {
                cam.stereoSeparation = stereoSeparation;
                cam.RenderToCubemap(cubemapLeftEye, 63, [Camera.MonoOrStereoscopicEye.Left](Camera.MonoOrStereoscopicEye.Left.html));
                cam.RenderToCubemap(cubemapRightEye, 63, [Camera.MonoOrStereoscopicEye.Right](Camera.MonoOrStereoscopicEye.Right.html));
            }
            else
            {
                cam.RenderToCubemap(cubemapLeftEye, 63, [Camera.MonoOrStereoscopicEye.Mono](Camera.MonoOrStereoscopicEye.Mono.html));
            }  
      
            //optional: convert cubemaps to equirect  
      
            if (equirect == null)
                return;  
      
            if (renderStereo)
            {
                cubemapLeftEye.ConvertToEquirect(equirect, [Camera.MonoOrStereoscopicEye.Left](Camera.MonoOrStereoscopicEye.Left.html));
                cubemapRightEye.ConvertToEquirect(equirect, [Camera.MonoOrStereoscopicEye.Right](Camera.MonoOrStereoscopicEye.Right.html));
            }
            else
            {
                cubemapLeftEye.ConvertToEquirect(equirect, [Camera.MonoOrStereoscopicEye.Mono](Camera.MonoOrStereoscopicEye.Mono.html));
            }
        }
    }
    

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

