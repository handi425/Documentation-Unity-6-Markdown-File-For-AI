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

# SerializeField

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

Force Unity to serialize a private field.

When Unity serializes your scripts, it only serializes public fields. If you
also want Unity to serialize your private fields you can add the
SerializeField attribute to those fields.  
  
Unity serializes all your script components, reloads the new assemblies, and
recreates your script components from the serialized versions. This
serialization is done with an internal Unity serialization system; not with
.NET's serialization functionality.  
  
The serialization system can do the following:

  * CAN serialize public non-static fields (of serializable types)
  * CAN serialize nonpublic non-static fields marked with the [SerializeField](SerializeField.html) attribute.
  * CANNOT serialize static fields.
  * CANNOT serialize properties.

**Serializable types**  
  
Unity can serialize fields of the following types:

  * All classes inheriting from UnityEngine.Object, for example GameObject, Component, MonoBehaviour, Texture2D, AnimationClip.
  * All basic data types, such as int, string, float, bool.
  * Some built-in types, such as Vector2, Vector3, Vector4, Quaternion, Matrix4x4, Color, Rect, LayerMask.
  * Arrays of a serializable type
  * Lists of a serializable type
  * Enums
  * Structs

For more information on serialization, see [Script
Serialization](../Manual/script-serialization.html).  
  
**Note:** If you put one element in a list (or array) twice, when the list
gets serialized, you'll get two copies of that element, instead of one copy
being in the new list twice.  
  
**Note** : If you want to serialize a custom Struct field, you must give the
Struct the [System.Serializable] attribute.  
  
**Hint:** Unity won't serialize Dictionary, however you could store a List<>
for keys and a List<> for values. See
[ISerializationCallbackReceiver](ISerializationCallbackReceiver.html) for an
example.  
  
Additional resources: NonSerialized,
[SerializeReference](SerializeReference.html), Serializable

    
    
    using UnityEngine;  
      
    public class SomePerson : [MonoBehaviour](MonoBehaviour.html)
    {
        //This field gets serialized because it is public.
        public string firstName = "John";  
      
        //This field does not get serialized because it is private.
        private int age = 40;  
      
        //This field gets serialized even though it is private
        //because it has the [SerializeField](SerializeField.html) attribute applied.
        [[SerializeField](SerializeField.html)]
        private bool hasHealthPotion = true;  
      
        void Start()
        {
            if (hasHealthPotion)
                [Debug.Log](Debug.Log.html)("Person's first name: " + firstName + " Person's age: " + age);
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

