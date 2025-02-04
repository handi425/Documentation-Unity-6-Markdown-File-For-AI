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

#  [GeometryUtility](GeometryUtility.html).TestPlanesAABB

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

public static bool TestPlanesAABB(Plane[] planes, [Bounds](Bounds.html)
bounds);

### Description

Returns true if bounds are inside the plane array.

Will return true if the bounding box is inside the planes or intersects any of
the planes.  
  
The TestPlanesAABB function uses the Plane array to test whether a bounding
box is in the frustum or not.  
You can use this function with CalculateFrustrumPlanes to test whether a
camera's view contains an object regardless of whether it is rendered or not.  
The test is conservative and can give false positive results. A bounding box
can intersect the planes outside of the frustum because the planes are
infinite and extend beyond the frustum volume. A typical false positive result
is produced by a big bounding box near the frustum edge or corner.  
  
Additional resources:
[GeometryUtility.CalculateFrustumPlanes](GeometryUtility.CalculateFrustumPlanes.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Detects manually if obj is being seen by the main camera  
      
        [GameObject](GameObject.html) obj;
        [Collider](Collider.html) objCollider;  
      
        [Camera](Camera.html) cam;
        [Plane](Plane.html)[] planes;  
      
        void Start()
        {
            cam = [Camera.main](Camera-main.html);
            planes = [GeometryUtility.CalculateFrustumPlanes](GeometryUtility.CalculateFrustumPlanes.html)(cam);
            objCollider =  GetComponent<[Collider](Collider.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([GeometryUtility.TestPlanesAABB](GeometryUtility.TestPlanesAABB.html)(planes, objCollider.bounds))
            {
                [Debug.Log](Debug.Log.html)(obj.name + " has been detected!");
            }
            else
            {
                [Debug.Log](Debug.Log.html)("Nothing has been detected");
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

