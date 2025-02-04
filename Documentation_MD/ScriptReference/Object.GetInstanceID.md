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

#  [Object](Object.html).GetInstanceID

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

[Switch to Manual](../Manual/class-Object.html "Go to Object Component in the
Manual")

## Declaration

public int GetInstanceID();

### Returns

**int** Returns the instance ID of the object.

### Description

Gets the instance ID of the object.

The instance ID of an object acts like a handle to the in-memory instance. It
is always unique, and never has the value 0. Objects loaded from file will be
assigned a positive Instance ID. Newly created objects will have a negative
Instance ID, and retain that negative value even if the object is later saved
to file. Therefore the sign of the InstanceID value is not a safe indicator
for whether or not the object is persistent.  
  
The ID changes between sessions of the player runtime and Editor. As such, the
ID is not reliable for performing actions that could span between sessions,
for example, loading an object state from a file.  
  
Additional resources:
[EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html),
[EditorUtility.IsPersistent](EditorUtility.IsPersistent.html)

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Create 10 game objects, which will have random Instance IDs
        void Awake()
        {
            for (int i = 0; i < 10; i++)
            {
                [GameObject](GameObject.html) go = new [GameObject](GameObject.html)("abc" + i.ToString("D3"));
            }
        }  
      
        // Find all the game objects and display their Instance IDs
        void Start()
        {
            Object[] allObjects = Object.FindObjectsOfType<[GameObject](GameObject.html)>();  
      
            foreach ([GameObject](GameObject.html) go in allObjects)
            {
                [Debug.Log](Debug.Log.html)(go + " is an active object " + go.GetInstanceID());
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

