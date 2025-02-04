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

# ManagedStrippingLevel

enumeration

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

Defines how aggressively Unity strips unused managed (C#) code.

When Unity builds your game or application it can strip unused code from the
managed dynamically linked libraries used in the project. Stripping code can
make the resulting executable significantly smaller, but can sometimes
mistakenly remove code that is actually used. The ManagedStrippingLevel Enum
defines the options you can use when specifying how aggressively Unity should
remove unused code.  
  
Additional resources:
[PlayerSettings.GetManagedStrippingLevel](PlayerSettings.GetManagedStrippingLevel.html),
[PlayerSettings.SetManagedStrippingLevel](PlayerSettings.SetManagedStrippingLevel.html)

### Properties

[Disabled](ManagedStrippingLevel.Disabled.html)| Do not strip any code.  
---|---  
[Low](ManagedStrippingLevel.Low.html)| Remove unreachable managed code to
reduce build size and Mono/IL2CPP build times.  
[Medium](ManagedStrippingLevel.Medium.html)| Run UnityLinker in a less
conservative mode than Low. This will further reduce code size beyond what Low
can achieve. However, this additional reduction may come with tradeoffs.
Possible side effects may include, having to maintain a custom link.xml file,
and some reflection code paths may not behave the same.  
[High](ManagedStrippingLevel.High.html)| UnityLinker will strip as much as
possible. This will further reduce code size beyond what Medium can achieve.
However, this additional reduction may come with tradeoffs. Possible side
effects may include, managed code debugging of some methods may no longer
work. You may need to maintain a custom link.xml file, and some reflection
code paths may not behave the same.  
[Minimal](ManagedStrippingLevel.Minimal.html)| The class libraries,
UnityEngine, and Windows Runtime assemblies will be stripped. All other
assemblies are copied.  
  
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

