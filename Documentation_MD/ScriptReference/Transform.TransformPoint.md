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

#  [Transform](Transform.html).TransformPoint

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

[Switch to Manual](../Manual/class-Transform.html "Go to Transform Component
in the Manual")

## Declaration

public [Vector3](Vector3.html) TransformPoint([Vector3](Vector3.html)
position);

### Description

Transforms `position` from local space to world space.

Note that the returned position is affected by scale. Use
[Transform.TransformDirection](Transform.TransformDirection.html) if you are
dealing with direction vectors.  
  
You can perform the opposite conversion, from world to local space using
[Transform.InverseTransformPoint](Transform.InverseTransformPoint.html).  
  
If you need to transform many points at once consider using
[Transform.TransformPoints](Transform.TransformPoints.html) instead as it is
much faster than repeatedly calling this function.  
  
Additional resources:
[Transform.TransformPoints](Transform.TransformPoints.html),
[Transform.TransformDirection](Transform.TransformDirection.html),
[Transform.TransformVector](Transform.TransformVector.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) someObject;
        public [Vector3](Vector3.html) thePosition;  
      
        void Start()
        {
            // Instantiate an object to the right of the current object
            thePosition = transform.TransformPoint([Vector3.right](Vector3-right.html) * 2);
            Instantiate(someObject, thePosition, someObject.transform.rotation);
        }
    }
    

* * *

## Declaration

public [Vector3](Vector3.html) TransformPoint(float x, float y, float z);

### Description

Transforms the position `x`, `y`, `z` from local space to world space.

Note that the returned position is affected by scale. Use
[Transform.TransformDirection](Transform.TransformDirection.html) if you are
dealing with direction vectors.  
  
You can perform the opposite conversion, from world to local space using
[Transform.InverseTransformPoint](Transform.InverseTransformPoint.html).  
  
If you need to transform many points at once consider using
[Transform.TransformPoints](Transform.TransformPoints.html) instead as it is
much faster than repeatedly calling this function.  
  
Additional resources:
[Transform.TransformPoints](Transform.TransformPoints.html),
[Transform.TransformDirection](Transform.TransformDirection.html),
[Transform.TransformVector](Transform.TransformVector.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) someObject;  
      
        void Start()
        {
            // Instantiate an object to the right of the current object
            [Vector3](Vector3.html) thePosition = transform.TransformPoint(2, 0, 0);
            Instantiate(someObject, thePosition, someObject.transform.rotation);
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

