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

#  [Collider](Collider.html).Raycast

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

public bool Raycast([Ray](Ray.html) ray, out [RaycastHit](RaycastHit.html)
hitInfo, float maxDistance);

### Parameters

ray | The starting point and direction of the ray.  
---|---  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit.  
maxDistance | The max length of the ray.  
  
### Returns

**bool** True when the ray intersects the collider, otherwise false.

### Description

Casts a [Ray](Ray.html) that ignores all Colliders except this one.

Additional resources: [RaycastHit](RaycastHit.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Collider](Collider.html) coll;  
      
        void Start()
        {
            coll = GetComponent<[Collider](Collider.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Move this object to the position clicked by the mouse.
            if ([Input.GetMouseButtonDown](Input.GetMouseButtonDown.html)(0))
            {
                [Ray](Ray.html) ray = Camera.main.ScreenPointToRay([Input.mousePosition](Input-mousePosition.html));
                [RaycastHit](RaycastHit.html) hit;  
      
                if (coll.Raycast(ray, out hit, 100.0f))
                {
                    transform.position = ray.GetPoint(100.0f);
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

