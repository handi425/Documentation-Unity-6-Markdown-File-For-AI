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

#  [GlobalObjectId](GlobalObjectId.html).GetGlobalObjectIdSlow

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

public static [GlobalObjectId](GlobalObjectId.html)
GetGlobalObjectIdSlow([Object](Object.html) targetObject);

### Parameters

targetObject | The object to obtain the unique identifier for.  
---|---  
  
### Returns

**GlobalObjectId** The `GlobalObjectId` for the object. If the conversion is
unsuccessful, then the `GlobalObjectId` is set to the default null ID. The
null ID has the string representation
`GlobalObjectId_V1-0-00000000000000000000000000000000-0-0`

### Description

Obtains the unique object identifiers based on an object reference.

This method is slow. Use it sparingly. To get unique identifiers for multiple
objects, it's recommended to use
[GlobalObjectId.GetGlobalObjectIdsSlow](GlobalObjectId.GetGlobalObjectIdsSlow.html)
instead of making multiple calls to this method. If you use this method in a
large project within other performance-sensitive contexts such as
[ISerializationCallbackReceiver.OnBeforeSerialize](ISerializationCallbackReceiver.OnBeforeSerialize.html)
or
[ISerializationCallbackReceiver.OnAfterDeserialize](ISerializationCallbackReceiver.OnAfterDeserialize.html),
it's strongly recommended to profile the performance impact.  
  
Additional resources:
[GlobalObjectId.GetGlobalObjectIdsSlow](GlobalObjectId.GetGlobalObjectIdsSlow.html),
[Object.GetInstanceID](Object.GetInstanceID.html)

* * *

## Declaration

public static [GlobalObjectId](GlobalObjectId.html) GetGlobalObjectIdSlow(int
instanceId);

### Parameters

instanceId | The instance ID of the object to obtain the unique identifier for.  
---|---  
  
### Returns

**GlobalObjectId** The `GlobalObjectId` for the object. If the conversion is
unsuccessful, then the `GlobalObjectId` is set to the default null ID. The
null ID has the string representation
`GlobalObjectId_V1-0-00000000000000000000000000000000-0-0`

### Description

Obtains the unique object identifiers based on an instance ID.

This method is slow. Use it sparingly. To get unique identifiers for multiple
objects, it's recommended to use
[GlobalObjectId.GetGlobalObjectIdsSlow](GlobalObjectId.GetGlobalObjectIdsSlow.html)
instead of making multiple calls to this method. If you use this method in a
large project within other performance-sensitive contexts such as
[ISerializationCallbackReceiver.OnBeforeSerialize](ISerializationCallbackReceiver.OnBeforeSerialize.html)
or
[ISerializationCallbackReceiver.OnAfterDeserialize](ISerializationCallbackReceiver.OnAfterDeserialize.html),
it's strongly recommended to profile the performance impact.  
  
Additional resources:
[GlobalObjectId.GetGlobalObjectIdsSlow](GlobalObjectId.GetGlobalObjectIdsSlow.html),
[Object.GetInstanceID](Object.GetInstanceID.html)

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

