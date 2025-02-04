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

#  [Camera](Camera.html).SetStereoViewMatrices

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

**Obsolete** Camera.SetStereoViewMatrices has been deprecated. Use
SetStereoViewMatrix(StereoscopicEye eye) instead.

## Declaration

public void SetStereoViewMatrices([Matrix4x4](Matrix4x4.html) leftMatrix,
[Matrix4x4](Matrix4x4.html) rightMatrix);

### Parameters

leftMatrix | View matrix for the stereo left eye.  
---|---  
rightMatrix | View matrix for the stereo right eye.  
  
### Description

Set custom view matrices for both eyes.

In most cases you should use the view matrices provided by the VR SDK to
ensure accurate stereoscopic rendering. However, in some scenarios it can be
useful to override the view matrices to achieve specific effects. For example,
custom view matrices would be required to implement binoculars in VR.  
  
If custom view matrices have been set, then the Camera will analyze the view
matrices to determine whether it is safe to use a single cull pass or if it
must separately cull each eye. Use
[Camera.areVRStereoViewMatricesWithinSingleCullTolerance](Camera-
areVRStereoViewMatricesWithinSingleCullTolerance.html) to find out which will
be used.  
  
Calling [Camera.ResetStereoViewMatrices](Camera.ResetStereoViewMatrices.html)
will revert the camera to using view matrices provided by the VR SDK. Note
that the [Camera.stereoSeparation](Camera-stereoSeparation.html) will not be
applied until you call
[Camera.ResetStereoViewMatrices](Camera.ResetStereoViewMatrices.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // Use this for initialization
        void Start()
        {
        }  
      
        // [Update](PlayerLoop.Update.html) is called once per frame
        void [Update](PlayerLoop.Update.html)()
        {
            [Camera](Camera.html) cam = GetComponent<[Camera](Camera.html)>();  
      
            [Matrix4x4](Matrix4x4.html) viewL = cam.worldToCameraMatrix;
            [Matrix4x4](Matrix4x4.html) viewR = cam.worldToCameraMatrix;  
      
            viewL[12] += 0.011f;
            viewR[12] -= 0.011f;
            cam.SetStereoViewMatrices(viewL, viewR);
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

