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

Virtual Texturing is experimental and not ready for production use. The
feature and documentation might be changed or removed in the future.

#  [Streaming](Rendering.VirtualTexturing.Streaming.html).RequestRegion

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

## Declaration

public static void RequestRegion([Material](Material.html) mat, int
stackNameId, [Rect](Rect.html) r, int mipMap, int numMips);

### Parameters

mat | The Material that contains the Virtual Texture Stack. The Virtual Texture Stacks contained in a Material are declared in the Material's Shader.  
---|---  
stackNameId | The unique identifier for the name of the Virtual Texture Stack, as declared in the Shader. To find the identifier for a given Shader property name, use [Shader.PropertyToID](Shader.PropertyToID.html).  
r | The rectangle in 0-1 UV space to make resident. Anything outside the [ 0...1 [ x [ 0...1 [ rectangle will be silently ignored.  
mipMap | The mip level to make resident. Mips are numbered from 0 (= full resolution) to n (= lowest resolution) where n is the mipmap level what is a single tile in size. Requesting invalid mips is silently ignored.  
numMips | The number of mip levels starting from 'mipMap' to make resident. Requesting invalid mips is silently ignored.  
  
### Description

Make a rectangle in UV space resident for a given Virtual Texture Stack.

The system will do it’s best to make this rectangle resident at the requested
resolution as fast as possible but due to time and memory constraints this
data may take a while to become resident or even never become resident. This
function should be called regularly (preferably every frame) to indicate the
continued interest in this data. When this function is no longer called the
requested area may be evicted from memory or only be available at a lower
resolution. See
[Streaming.RequestRegion](Rendering.VirtualTexturing.Streaming.RequestRegion.html)
for an example using this function.  
  
The following example requests the 1024 x 1024 pixel mipmap level of a given
Virtual Texture Stack.

    
    
    using UnityEngine;  
      
    public class GetStackSizeSample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Material](Material.html) targetMaterial;
        public string stackName;
        private bool m_ShouldRequestRegionForVT = false;
        const float desiredMipmapLevelPixelSize = 1024f;  
      
        private void OnBecameVisible()
        {
            m_ShouldRequestRegionForVT = true;
        }  
      
        private void OnBecameInvisible()
        {
            m_ShouldRequestRegionForVT = false;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (m_ShouldRequestRegionForVT)
            {
                int stackPropertyId = [Shader.PropertyToID](Shader.PropertyToID.html)(stackName);  
      
                // Get size in pixels of the stack.
                int width, height;
                UnityEngine.Rendering.VirtualTexturing.Streaming.GetTextureStackSize(targetMaterial, stackPropertyId, out width, out height);  
      
                // Calculate the index of the 1024 x 1024 mipmap level.
                int powerOfTwoExponent_RealSize = (int)[Mathf.Max](Mathf.Max.html)([Mathf.Log](Mathf.Log.html)(width, 2f), [Mathf.Log](Mathf.Log.html)(height, 2f));
                int powerOfTwoExponent_DesiredSize = (int)[Mathf.Log](Mathf.Log.html)(desiredMipmapLevelPixelSize, 2f);  
      
                // The difference between the real size and the desired size is the same as the mipmap level we want.
                // For example, to get a 1024 x 1024 mipmap level from a 4096 x 4096 texture, use mipmap level 2.
                // If the mipmap level is larger than the texture, fall back to the original texture size at mipmap level 0.
                int mipmapLevel = [Mathf.Max](Mathf.Max.html)(powerOfTwoExponent_RealSize - powerOfTwoExponent_DesiredSize, 0);  
      
                // [Request](PackageManager.Requests.Request.html) this mipmap level to be made resident.
                UnityEngine.Rendering.VirtualTexturing.Streaming.RequestRegion(targetMaterial, stackPropertyId, new [Rect](Rect.html)(0.0f, 0.0f, 1.0f, 1.0f), mipmapLevel, UnityEngine.Rendering.VirtualTexturing.System.AllMips);
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

