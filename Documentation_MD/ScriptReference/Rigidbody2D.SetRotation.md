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

#  [Rigidbody2D](Rigidbody2D.html).SetRotation

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

public void SetRotation(float angle);

### Parameters

angle | The rotation of the Rigidbody (in degrees).  
---|---  
  
### Description

Sets the rotation of the [Rigidbody2D](Rigidbody2D.html) to `angle` (given in
degrees).

Additional resources: [Rigidbody2D.rotation](Rigidbody2D-rotation.html) and
[Rigidbody2D.MoveRotation](Rigidbody2D.MoveRotation.html).

    
    
    using UnityEngine;  
      
    // [Rotate](UIElements.Rotate.html) rigidBody2D every frame.
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Rigidbody2D](Rigidbody2D.html) rigidBody2D;
        public float rotation = 0.0f;  
      
        void Start()
        {
            rigidBody2D = GetComponent<[Rigidbody2D](Rigidbody2D.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            rigidBody2D.SetRotation(rotation);  
      
            rotation += 1.0f;
        }
    }
    

* * *

## Declaration

public void SetRotation([Quaternion](Quaternion.html) rotation);

### Parameters

rotation | Full 3D rotation used to extract only the z-axis rotation.  
---|---  
  
### Description

Sets the rotation of the [Rigidbody2D](Rigidbody2D.html) to the z-axis
rotation extracted from the full 3D `rotation`.

The z-axis rotation is extracted from the given [Quaternion](Quaternion.html)
`rotation` and used as the rotation for [Rigidbody2D](Rigidbody2D.html). It is
important to understand that the full 3D rotation isn't used because the
[Rigidbody2D](Rigidbody2D.html) only has a single degree of rotational freedom
around the z-axis.

    
    
    using UnityEngine;  
      
    // [Rotate](UIElements.Rotate.html) rigidBody2D every frame.
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Rigidbody2D](Rigidbody2D.html) rigidBody2D;
        public float rotation = 0.0f;  
      
        void Start()
        {
            rigidBody2D = GetComponent<[Rigidbody2D](Rigidbody2D.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var quaternionRotation = [Quaternion.Euler](Quaternion.Euler.html)(0f, 0f, rotation);
            rigidBody2D.SetRotation(rotation);  
      
            rotation += 1.0f;
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

