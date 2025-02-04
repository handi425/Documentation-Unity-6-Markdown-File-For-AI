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

**Removed**  

#  [Security](Security.html).LoadAndVerifyAssembly

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

**Obsolete** This was an internal method which is no longer used.

## Declaration

public static [Compilation.Assembly](Compilation.Assembly.html)
LoadAndVerifyAssembly(byte[] assemblyData, string authorizationKey);

**Obsolete** This was an internal method which is no longer used.

## Declaration

public static [Compilation.Assembly](Compilation.Assembly.html)
LoadAndVerifyAssembly(byte[] assemblyData);

### Parameters

assemblyData | Assembly to verify.  
---|---  
authorizationKey | Public key used to verify assembly.  
  
### Returns

**Assembly** Loaded, verified, assembly, or null if the assembly cannot be
verfied.

### Description

Loads an assembly and checks that it is allowed to be used in the webplayer.
(Web Player is no Longer Supported).

This function used to relate to the chain of trust system used by the
webplayer in earlier versions of unity.  
  
The single argument version of this API will always issue an error message. An
authorisation key is always needed.  
  
Note that web player is not supported from 5.4.0, so this function no longer
serves a purpose and will be deprecated.

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

