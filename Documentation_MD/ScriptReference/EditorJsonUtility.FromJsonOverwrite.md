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

#  [EditorJsonUtility](EditorJsonUtility.html).FromJsonOverwrite

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

public static void FromJsonOverwrite(string json, object objectToOverwrite);

### Parameters

json | The JSON representation of the object.  
---|---  
objectToOverwrite | The object to overwrite.  
  
### Description

Overwrite data in an object by reading from its JSON representation.

This is similar to
[JsonUtility.FromJsonOverwrite](JsonUtility.FromJsonOverwrite.html), but it
supports any engine object.  
  
Note that using this method with a struct may not do what you expect because
structs are passed to the method by value and not by reference. This means
that instead of the method overwriting your original struct, a boxed copy of
the struct is passed into the method and overwritten. You can avoid this by
making your own boxed copy of the struct to pass into the method and then
copying the values back again after the method returns. See example below.  
  
Even when you do this, Unity’s built-in structs (such as
[Vector3](Vector3.html) or [Bounds](Bounds.html)) cannot be directly passed to
the method, so you must enclose Unity’s built-in structs inside a wrapper
class or struct.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [System.Serializable]
    struct MyStruct
    {
        public int value;
    }  
      
    public class StructExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            MyStruct myStruct = new MyStruct();
            object boxedStruct = myStruct;
            var json = @"{ ""value"" : 42 }";
            [EditorJsonUtility.FromJsonOverwrite](EditorJsonUtility.FromJsonOverwrite.html)(json, boxedStruct);
            myStruct = (MyStruct)boxedStruct;
            [Debug.Log](Debug.Log.html)("myStruct.value = " + myStruct.value);
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

