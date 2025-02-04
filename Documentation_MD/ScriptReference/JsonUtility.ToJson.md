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

#  [JsonUtility](JsonUtility.html).ToJson

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

public static string ToJson(object obj);

## Declaration

public static string ToJson(object obj, bool prettyPrint);

### Parameters

obj | The object to convert to JSON form.  
---|---  
prettyPrint | If true, format the output for readability. If false, format the output for minimum size. Default is false.  
  
### Returns

**string** The object's data in JSON format.

### Description

Generate a JSON representation of the public fields of an object.

Internally, this method uses the Unity serializer; therefore the object you
pass in must be supported by the serializer: it must be a MonoBehaviour,
ScriptableObject, or plain class/struct with the Serializable attribute
applied. The types of fields that you want to be included must be supported by
the serializer; unsupported fields will be ignored, as will private fields,
static fields, and fields with the NonSerialized attribute applied.  
  
Any plain class or structure is supported, as well as classes derived from
MonoBehaviour or ScriptableObject. Other engine types are not supported. (In
the Editor only, you can use
[EditorJsonUtility.ToJson](EditorJsonUtility.ToJson.html) to serialize other
engine types to JSON).  
  
If the object contains fields with references to other Unity objects, those
references are serialized by recording the InstanceID for each referenced
object. Because the Instance ID acts like a handle to the in-memory object
instance, the JSON string can only be deserialized back during the same
session of the Unity engine.  
  
Note that while it is possible to pass primitive types to this method, the
results may not be what you expect; instead of serializing them directly, the
method will attempt to serialize their public instance fields, producing an
empty object as a result. Similarly, passing an array to this method will not
produce a JSON array containing each element, but an object containing the
public fields of the array object itself (of which there are none). To
serialize the actual content of an array or primitive type, it is necessary to
wrap it in a class or struct.  
  
This method can be called from background threads. You should not alter the
object that you pass to this function while it is still executing.  
  
Additional resources: [MonoBehaviour](MonoBehaviour.html),
[ScriptableObject](ScriptableObject.html),
[Object.GetInstanceID](Object.GetInstanceID.html)

    
    
    using UnityEngine;  
      
    public class PlayerState : [MonoBehaviour](MonoBehaviour.html)
    {
        public string playerName;
        public int lives;
        public float health;  
      
        public string SaveToString()
        {
            return [JsonUtility.ToJson](JsonUtility.ToJson.html)(this);
        }  
      
        // Given:
        // playerName = "Dr Charles"
        // lives = 3
        // health = 0.8f
        // SaveToString returns:
        // {"playerName":"Dr Charles","lives":3,"health":0.8}
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

