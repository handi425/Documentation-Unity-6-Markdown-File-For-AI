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

#  [Mesh](Mesh.html).GetUVDistributionMetric

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

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

## Declaration

public float GetUVDistributionMetric(int uvSetIndex);

### Parameters

uvSetIndex | UV set index to return the UV distibution metric for. 0 for first.  
---|---  
  
### Returns

**float** Average of triangle area / uv area.

### Description

The UV distribution metric can be used to calculate the desired mipmap level
based on the position of the camera.

The example code shows how this value can be used with some camera properties
to calculate a required mipmap level.

    
    
    using UnityEngine;  
      
    public class MyMipmapClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Vector3](Vector3.html) m_CameraPosition;
        private float m_CameraEyeToScreenDistanceSquared;  
      
        private float m_MeshUVDistributionMetric;
        private float m_TexelCount;
        private [Texture2D](Texture2D.html) m_Texture;  
      
        public void SetView([Vector3](Vector3.html) cameraPosition, float cameraHalfAngle, float screenHalfHeight, float aspectRatio)
        {
            m_CameraPosition = cameraPosition;
            m_CameraEyeToScreenDistanceSquared = [Mathf.Pow](Mathf.Pow.html)(screenHalfHeight / [Mathf.Tan](Mathf.Tan.html)(cameraHalfAngle), 2.0f);  
      
            // [Switch](PlayerSettings.Switch.html) to using the horizontal dimension if larger
            if (aspectRatio > 1.0f)    // Width is larger than height
                m_CameraEyeToScreenDistanceSquared *= aspectRatio;
        }  
      
        public void SetView([Camera](Camera.html) camera)
        {
            float cameraHA = [Mathf.Deg2Rad](Mathf.Deg2Rad.html) * camera.fieldOfView * 0.5f;
            float screenHH = (float)camera.pixelHeight * 0.5f;
            SetView(camera.transform.position, cameraHA, screenHH, camera.aspect);
        }  
      
        private int CalculateMipmapLevel([Bounds](Bounds.html) bounds, float uvDistributionMetric, float texelCount)
        {
            // based on  http://web.cse.ohio-state.edu/~crawfis.3/cse781/Readings/MipMapLevels-Blog.html
            // screenArea = worldArea * (ScreenPixels/(D*tan(FOV)))^2
            // mip = 0.5 * log2 (uvArea / screenArea)
            float dSq = bounds.SqrDistance(m_CameraPosition);
            if (dSq < 1e-06)
                return 0;  
      
            // uvDistributionMetric is the average of triangle area / uv area (a ratio from world space triangle area to normalised uv area)
            // - triangle area is in world space
            // - uv area is in normalised units (0->1 rather than 0->texture size)  
      
            // m_CameraEyeToScreenDistanceSquared / dSq is the ratio of screen area to world space area  
      
            float v = (texelCount * dSq) / (uvDistributionMetric * m_CameraEyeToScreenDistanceSquared);
            float desiredMipLevel = 0.5f * [Mathf.Log](Mathf.Log.html)(v, 2);  
      
            return (int)desiredMipLevel;
        }  
      
        // Pick the larger two scales of the 3 components and multiply together
        float GetLargestAreaScale(float x, float y, float z)
        {
            if (x > y)
            {
                if (y > z)
                    return x * y;
                else
                    return x * z;
            }
            else // x <= y
            {
                if (x < z)
                    return y * z;
                else
                    return x * y;
            }
        }  
      
        public void Start()
        {
            [Mesh](Mesh.html) mesh = GetComponent<[MeshFilter](MeshFilter.html)>().sharedMesh;
            m_MeshUVDistributionMetric = mesh.GetUVDistributionMetric(0);  
      
            // If the mesh has a transform scale or uvscale it would need to be applied here  
      
            // [Transform](Transform.html) scale:
            // Use two scale values as we need an 'area' scale.
            // Use the two largest component to usa a more conservative selection and pick the higher resolution mip
            m_MeshUVDistributionMetric *= GetLargestAreaScale(transform.lossyScale.x, transform.lossyScale.y, transform.lossyScale.z);  
      
            // To determine uv scale for a material use [Material.GetTextureScale](Material.GetTextureScale.html)
            // If there is a uv scale to apply then divide the m_MeshUVDistributionMetric by (uvScale.x * uvScale.y)  
      
            m_TexelCount = m_Texture.width * m_Texture.height;
        }  
      
        public void [Update](PlayerLoop.Update.html)()
        {
            SetView([Camera.main](Camera-main.html));  
      
            m_Texture.requestedMipmapLevel = CalculateMipmapLevel(GetComponent<[Renderer](Renderer.html)>().bounds, m_MeshUVDistributionMetric, m_TexelCount);
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

