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

#  [Vector3](Vector3.html).Project

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

public static [Vector3](Vector3.html) Project([Vector3](Vector3.html) vector,
[Vector3](Vector3.html) onNormal);

### Description

Projects a vector onto another vector.

To understand vector projection, imagine that `onNormal` is resting on a line
pointing in its direction. Somewhere along that line will be the nearest point
to the tip of `vector`. The projection is just `onNormal` rescaled so that it
reaches that point on the line.  
  
![](../StaticFiles/ScriptRefImages/Vec3ProjectDiagram.png)  
  
The function will return a zero vector if `onNormal` is almost zero.  
  
An example of the usage of projection is a rail-mounted gun that should slide
so that it gets as close as possible to a target object. The projection of the
target heading along the direction of the rail can be used to move the gun by
applying a force to a rigidbody, say.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Slide([Transform](Transform.html) target, [Vector3](Vector3.html) railDirection)
        {
            [Vector3](Vector3.html) heading = target.position - transform.position;
            [Vector3](Vector3.html) force = [Vector3.Project](Vector3.Project.html)(heading, railDirection);  
      
            GetComponent<[Rigidbody](Rigidbody.html)>().AddForce(force);
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

