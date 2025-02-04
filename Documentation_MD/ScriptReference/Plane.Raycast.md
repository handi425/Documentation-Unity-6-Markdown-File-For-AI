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

#  [Plane](Plane.html).Raycast

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

public bool Raycast([Ray](Ray.html) ray, out float enter);

### Description

Intersects a ray with the plane.

This function sets `enter` to the distance along the ray, where it intersects
the plane. If the ray is parallel to the plane, function returns `false` and
sets `enter` to zero. If the ray is pointing in the opposite direction than
the plane, function returns `false` and sets `enter` to the distance along the
ray (negative value).

    
    
    //This script detects mouse clicks on a plane using [Plane.Raycast](Plane.Raycast.html).
    //In this example, the plane is set to the [Camera](Camera.html)'s x and y position, but you can set the z position so the plane is in front of your [Camera](Camera.html).
    //The normal of the plane is set to facing forward so it is facing the [Camera](Camera.html), but you can change this to suit your own needs.  
      
    //In your [GameObject](GameObject.html)'s Inspector, set your clickable distance and attach a cube [GameObject](GameObject.html) in the appropriate fields  
      
    using UnityEngine;  
      
    public class PlaneRayExample : [MonoBehaviour](MonoBehaviour.html)
    {
        //Attach a cube [GameObject](GameObject.html) in the Inspector before entering Play [Mode](Scripting.GarbageCollector.Mode.html)
        public [GameObject](GameObject.html) m_Cube;  
      
        //This is the distance the clickable plane is from the camera. Set it in the Inspector before running.
        public float m_DistanceZ;  
      
        [Plane](Plane.html) m_Plane;
        [Vector3](Vector3.html) m_DistanceFromCamera;  
      
        void Start()
        {
            //This is how far away from the [Camera](Camera.html) the plane is placed
            m_DistanceFromCamera = new [Vector3](Vector3.html)(Camera.main.transform.position.x, Camera.main.transform.position.y, Camera.main.transform.position.z - m_DistanceZ);  
      
            //Create a new plane with normal (0,0,1) at the position away from the camera you define in the Inspector. This is the plane that you can click so make sure it is reachable.
            m_Plane = new [Plane](Plane.html)([Vector3.forward](Vector3-forward.html), m_DistanceFromCamera);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Detect when there is a mouse click
            if ([Input.GetMouseButton](Input.GetMouseButton.html)(0))
            {
                //Create a ray from the Mouse click position
                [Ray](Ray.html) ray = Camera.main.ScreenPointToRay([Input.mousePosition](Input-mousePosition.html));  
      
                //Initialise the enter variable
                float enter = 0.0f;  
      
                if (m_Plane.Raycast(ray, out enter))
                {
                    //Get the point that is clicked
                    [Vector3](Vector3.html) hitPoint = ray.GetPoint(enter);  
      
                    //Move your cube [GameObject](GameObject.html) to the point where you clicked
                    m_Cube.transform.position = hitPoint;
                }
            }
        }
    }
    

Additional resources: [Physics.Raycast](Physics.Raycast.html).

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

