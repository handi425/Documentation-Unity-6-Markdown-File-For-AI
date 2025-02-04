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

#
[ContentBuildInterface](Build.Content.ContentBuildInterface.html).CalculateBuildUsageTags

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

public static void CalculateBuildUsageTags(ObjectIdentifier[] objectIDs,
ObjectIdentifier[] dependentObjectIDs,
[Build.Content.BuildUsageTagGlobal](Build.Content.BuildUsageTagGlobal.html)
globalUsage,
[Build.Content.BuildUsageTagSet](Build.Content.BuildUsageTagSet.html)
usageSet);

## Declaration

public static void CalculateBuildUsageTags(ObjectIdentifier[] objectIDs,
ObjectIdentifier[] dependentObjectIDs,
[Build.Content.BuildUsageTagGlobal](Build.Content.BuildUsageTagGlobal.html)
globalUsage,
[Build.Content.BuildUsageTagSet](Build.Content.BuildUsageTagSet.html)
usageSet, [Build.Content.BuildUsageCache](Build.Content.BuildUsageCache.html)
usageCache);

### Parameters

objectIDs | Objects that will have their build usage calculated.  
---|---  
dependentObjectIDs | Objects that reference the Objects being calculated.  
globalUsage | Lighting information used by the build.  
usageSet | The BuildUsageTagSet where the calculated usage information will be stored.  
usageCache | Optional cache object to use for improving performance with multiple calls to this api.  
  
### Description

Calculates the build usage of a set of objects.

Internal use only. See note on
[ContentBuildInterface](Build.Content.ContentBuildInterface.html).  
  
To calculate how any given Object is being used in a build, we need two pieces
of information. First, we need to know that Object's dependents, or in other
words, what references that Object. For example, for a Shader, we would need
to know the list Materials that reference that shader. Second, we need the
combined lighting information for Scenes where the Object can be used. Using
these two pieces of information, we calculate the correct usage information
for an Object, and then store that information in the
[BuildUsageTagSet](Build.Content.BuildUsageTagSet.html).

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

