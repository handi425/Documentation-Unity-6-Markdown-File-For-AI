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

**Method group is Obsolete**  

**Experimental** : this API is experimental and might be changed or removed in
the future.

#
[ArrayEntries<T0>](Profiling.Memory.Experimental.ArrayEntries_1.html).GetEntries

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

**Obsolete** This API is outdated and will be removed. Please check out the
Memory Profiler Package
(https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/).

## Declaration

public void GetEntries(uint indexStart, uint numEntries, ref T[] dataOut);

### Parameters

indexStart | Index to start indexing the entries.  
---|---  
numEntries | Number of elements to retrieve.  
dataOut | An array to store the returned data in.  
  
### Description

Retrieves a subset of entries in an array.

GetEntries retrieves the number of entries specified by the numEntries
parameter, starting at index as specified by the indexStart Parameter. The
entries are written to the array specified by the dataOut parameter.  
  
The method throws an IOException if you try to retrieve entries past the end
of the of array (entryIndex plus numEntries is greater than the number of
entries in the array) or the number of entries to retrieve is greater than the
size of the dataOut array.

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

