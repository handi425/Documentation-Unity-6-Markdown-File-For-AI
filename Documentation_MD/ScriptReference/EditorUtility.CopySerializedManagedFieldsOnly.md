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

#  [EditorUtility](EditorUtility.html).CopySerializedManagedFieldsOnly

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

public static void CopySerializedManagedFieldsOnly(object source, object
dest);

### Parameters

source | The object to copy data from.  
---|---  
dest | The object to copy data to.  
  
### Description

Copies the serializable fields from one managed object to another.

This is similar to CopySerialized, but you can use it with any two managed
objects, rather than two instances of the same Object subclass.  
  
`CopySerializedManagedFieldsOnly` copies all fields supported by the Unity
serializer. If the destination object is not of the same class as the source
object, then the function matches fields by name, or by using the
FormerlySerializedAs attribute. The function does not modify any fields on the
destination object which are not serializable, or which do not have
corresponding fields in the source object.  
  
If the source object implements the
[ISerializationCallbackReceiver](ISerializationCallbackReceiver.html)
interface, then its OnBeforeSerialize method is called before any data is
read. Similarly, if the destination object implements the
[ISerializationCallbackReceiver](ISerializationCallbackReceiver.html), then
its OnAfterDeserialize method is called after data has been copied into its
fields.  
  
`CopySerializedManagedFieldsOnly` only copies fields defined in managed code.
This means that if you attempt to copy engine objects such as
[Transform](Transform.html) or [Light](Light.html),
`CopySerializedManagedFieldsOnly` does not copy any data, since all of their
serializable fields are defined in native code.

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

