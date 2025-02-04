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

#  [GenericBindingUtility](Animations.GenericBindingUtility.html).SetValues

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

public static void SetValues(NativeArray<BoundProperty> boundProperties,
NativeArray<float> values);

## Declaration

public static void SetValues(NativeArray<BoundProperty> boundProperties,
NativeArray<int> values);

### Parameters

boundProperties | The list of [BoundProperty](Animations.BoundProperty.html) to set the values for.  
---|---  
values | The list of float or integer values to set.  
  
### Description

Sets the float or integer value for each [[BoundProperty].

This method throws an ArgumentException if the NativeArray is not yet created.  
  
This method throws an ArgumentException if the indices list does not match the
length of the boundProperties list.

* * *

## Declaration

public static void SetValues(NativeArray<BoundProperty> boundProperties,
NativeArray<int> indices, NativeArray<float> values);

## Declaration

public static void SetValues(NativeArray<BoundProperty> boundProperties,
NativeArray<int> indices, NativeArray<int> values);

### Parameters

boundProperties | The list of [BoundProperty](Animations.BoundProperty.html) to set the values for.  
---|---  
indices | The list of indices where each [BoundProperty](Animations.BoundProperty.html) value will be read.  
values | The list of float or integer values.  
  
### Description

Sets the float/integer values for each [[BoundProperty] and uses the value at
the index define in indices.

This method throws an ArgumentException if the NativeArray is not yet created.  
  
This method throws an ArgumentException if the indices list does not match the
length of the boundProperties list.  
  
This method throws an IndexOutOfRangeException if an index in the indices list
is out of range.

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

