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

#  [Time](Time.html).maximumDeltaTime

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

public static float maximumDeltaTime;

### Description

The maximum value of [Time.deltaTime](Time-deltaTime.html) in any given frame.
This is a time in seconds that limits the increase of [Time.time](Time-
time.html) between two frames.

When a very slow frame happens, maximumDeltaTime limits the value of
[Time.deltaTime](Time-deltaTime.html) in the following frame to avoid
undesirable side-effects from very large deltaTime values.  
  
The recommended value depends on the desired characteristics of your
application when frame hitches occur. maximumDeltaTime has these practical
effects:

  * Bounds the maximum number of times Unity executes [MonoBehaviour.FixedUpdate](MonoBehaviour.FixedUpdate.html) in a frame to maximumDeltaTime / fixedDeltaTime.
  * Sets a limit on the value of [Time.deltaTime](Time-deltaTime.html) which is commonly used to drive dynamic parts of the application like player movement. This controls whether and how much the application stutters or speeds up after a frame hitch.

A low value of maximumDeltaTime might prevent a long series of frame hitches
in applications with long
[MonoBehaviour.FixedUpdate](MonoBehaviour.FixedUpdate.html) phases. In these
cases, a long frame causes multiple executions of FixedUpdate phases in the
following frame, which causes another long frame and so on.  
  
**Important:** Unity enforces that maximumDeltaTime is always at least as
large as [Time.fixedDeltaTime](Time-fixedDeltaTime.html).  
  
See [Time and Frame Rate Management](../Manual/managing-time-and-frame-
rate.html) in the User Manual for more information about how this property
relates to the other Time properties.

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

