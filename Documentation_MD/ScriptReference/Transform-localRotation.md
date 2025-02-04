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

#  [Transform](Transform.html).localRotation

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

public [Quaternion](Quaternion.html) localRotation;

### Description

The rotation of the transform relative to the transform rotation of the
parent.

Unity stores rotations as Quaternions internally. To rotate an object, use
[Transform.Rotate](Transform.Rotate.html). Use
[Transform.localEulerAngles](Transform-localEulerAngles.html) for modifying
the rotation as euler angles.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Example()
        {
            transform.localRotation = [Quaternion.identity](Quaternion-identity.html);
        }
    }
    

Another example:

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // [Rotate](UIElements.Rotate.html) a cylinder around the x and z axes. [Switch](PlayerSettings.Switch.html) from one to the other
    // when the rotation in the current axis reaches 360 degrees.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        private float x;
        private float z;
        private bool rotateX;
        private float rotationSpeed;  
      
        void Start()
        {
            x = 0.0f;
            z = 0.0f;
            rotateX = true;
            rotationSpeed = 75.0f;
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            if (rotateX == true)
            {
                x += [Time.deltaTime](Time-deltaTime.html) * rotationSpeed;  
      
                if (x > 360.0f)
                {
                    x = 0.0f;
                    rotateX = false;
                }
            }
            else
            {
                z += [Time.deltaTime](Time-deltaTime.html) * rotationSpeed;  
      
                if (z > 360.0f)
                {
                    z = 0.0f;
                    rotateX = true;
                }
            }  
      
            transform.localRotation = [Quaternion.Euler](Quaternion.Euler.html)(x, 0, z);
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

