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

#  [EditorJsonUtility](EditorJsonUtility.html).ToJson

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

Generate a JSON representation of an object.

This is similar to [JsonUtility.ToJson](JsonUtility.ToJson.html), but it
supports any engine object. The output is similar to the properties exposed
via the [SerializedObject](SerializedObject.html) API, or as found in the
YAML-serialized form of the object.  
  
If the object contains fields with references to other Unity objects, those
references are serialized by recording the asset guid and local file id for
each reference. This string can be saved, then deserialized in another session
of the Unity Editor, and the references are resolved correctly. However only
objects that are located in an non-scene asset file can be referenced.
References to objects within a scene, including the same scene, will not be
serialized.  
  
Additional resources: [JsonUtility.ToJson](JsonUtility.ToJson.html),
[AssetDatabase.TryGetGUIDAndLocalFileIdentifier](AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)

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

