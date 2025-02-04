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

#  [Vector2](Vector2.html).operator -

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

public static [Vector2](Vector2.html) operator -([Vector2](Vector2.html) a,
[Vector2](Vector2.html) b);

### Returns

**Vector2** The difference between the two vectors, returned as a Vector2
struct.

### Description

Subtracts one vector from another.

Subtracts each component of `b` from `a`.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create two vectors.
            [Vector2](Vector2.html) A = new [Vector2](Vector2.html)(1, 2);
            [Vector2](Vector2.html) B = new [Vector2](Vector2.html)(3, 2);
            
            // Subtract vector B from vector A.
            [Vector2](Vector2.html) C = A - B;
            
            // Print the result.
            print(C);
        }
    }
    

* * *

public static [Vector2](Vector2.html) operator -([Vector2](Vector2.html) a);

### Returns

**Vector2** The negative of the vector, returned as a Vector2 struct.

### Description

Negates a vector.

Each component in the vector is negated, to obtain its negative value. The
negative of a vector has the same magnitude but opposite direction

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
           // Create a vector.
           [Vector2](Vector2.html) A = new [Vector2](Vector2.html)(1, 2);
           
           // Find the negative value.
           [Vector2](Vector2.html) B = - A;
      
           // Print the result.
            print(B + " is the negative of " + A);
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

