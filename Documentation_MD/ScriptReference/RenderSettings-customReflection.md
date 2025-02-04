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

**Method group is Obsolete**  

#  [RenderSettings](RenderSettings.html).customReflection

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

**Obsolete** RenderSettings.customReflection has been deprecated in favor of
RenderSettings.customReflectionTexture. public static [Cubemap](Cubemap.html)
customReflection;

### Description

Custom specular reflection cubemap.

Specifies a cubemap for use as a default specular reflection.  
  
Additional resources: [defaultReflectionMode](RenderSettings-
defaultReflectionMode.html).

    
    
    using UnityEngine;  
      
    // This example creates and uses a real-time Reflection Probe to update a [Cubemap](Cubemap.html). The [Cubemap](Cubemap.html) is then used as a default specular reflection.
    public class UpdateDefaultReflection : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ReflectionProbe](ReflectionProbe.html) probeComponent = null;
        private [Cubemap](Cubemap.html) cubemap = null;
        private int renderId = -1;  
      
        void Start()
        {
            [GameObject](GameObject.html) probeGameObject = new [GameObject](GameObject.html)("Default Reflection Probe");  
      
            // Use a location such that the new Reflection Probe will not interfere with other Reflection Probes in the [Scene](SceneManagement.Scene.html).
            probeGameObject.transform.position = new [Vector3](Vector3.html)(0, -1000, 0);  
      
            // Create a Reflection Probe that only contains the [Skybox](Skybox.html). The [Update](PlayerLoop.Update.html) function controls the Reflection Probe refresh.
            probeComponent = probeGameObject.AddComponent<[ReflectionProbe](ReflectionProbe.html)>() as [ReflectionProbe](ReflectionProbe.html);
            probeComponent.resolution = 256;
            probeComponent.size = new [Vector3](Vector3.html)(1, 1, 1);
            probeComponent.cullingMask = 0;
            probeComponent.clearFlags = UnityEngine.Rendering.ReflectionProbeClearFlags.Skybox;
            probeComponent.mode = UnityEngine.Rendering.ReflectionProbeMode.Realtime;
            probeComponent.refreshMode = UnityEngine.Rendering.ReflectionProbeRefreshMode.ViaScripting;
            probeComponent.timeSlicingMode = UnityEngine.Rendering.ReflectionProbeTimeSlicingMode.NoTimeSlicing;  
      
            // A cubemap is used as a default specular reflection.
            cubemap = new [Cubemap](Cubemap.html)(probeComponent.resolution, probeComponent.hdr ? [TextureFormat.RGBAHalf](TextureFormat.RGBAHalf.html) : [TextureFormat.RGBA32](TextureFormat.RGBA32.html), true);
        }  
      
        // The [Update](PlayerLoop.Update.html) function refreshes the Reflection Probe and copies the result to the default specular reflection [Cubemap](Cubemap.html).
        void [Update](PlayerLoop.Update.html)()
        {
            // The texture associated with the real-time Reflection Probe is a render target and RenderSettings.customReflection is a [Cubemap](Cubemap.html). We have to check the support if copying from render targets to Textures is supported.
            if (([SystemInfo.copyTextureSupport](SystemInfo-copyTextureSupport.html) & UnityEngine.Rendering.CopyTextureSupport.RTToTexture) != 0)
            {
                // Wait until previous RenderProbe is finished before we refresh the Reflection Probe again.
                // renderId is a token used to figure out when the refresh of a Reflection Probe is finished. The refresh of a Reflection Probe can take mutiple frames when time-slicing is used.
                if (renderId == -1 || probeComponent.IsFinishedRendering(renderId))
                {
                    if (probeComponent.IsFinishedRendering(renderId))
                    {
                        // After the previous RenderProbe is finished, we copy the probe's texture to the cubemap and set it as a custom reflection in [RenderSettings](RenderSettings.html).
                        [Graphics.CopyTexture](Graphics.CopyTexture.html)(probeComponent.texture, cubemap as [Texture](Texture.html));  
      
                        RenderSettings.customReflection = cubemap;
                        [RenderSettings.defaultReflectionMode](RenderSettings-defaultReflectionMode.html) = UnityEngine.Rendering.DefaultReflectionMode.Custom;
                    }  
      
                    renderId = probeComponent.RenderProbe();
                }
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

