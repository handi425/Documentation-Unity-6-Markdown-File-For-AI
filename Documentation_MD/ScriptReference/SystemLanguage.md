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

# SystemLanguage

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

The language the user's operating system is running in. Returned by
Application.systemLanguage.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            //This checks if your computer's operating system is in the French language
            if ([Application.systemLanguage](Application-systemLanguage.html) == [SystemLanguage.French](SystemLanguage.French.html))
            {
                //Outputs into console that the system is French
                [Debug.Log](Debug.Log.html)("This system is in French. ");
            }
            //Otherwise, if the system is English, output the message in the console
            else if ([Application.systemLanguage](Application-systemLanguage.html) == [SystemLanguage.English](SystemLanguage.English.html))
            {
                [Debug.Log](Debug.Log.html)("This system is in English. ");
            }
        }
    }
    

### Properties

[Afrikaans](SystemLanguage.Afrikaans.html)| Afrikaans.  
---|---  
[Arabic](SystemLanguage.Arabic.html)| Arabic.  
[Basque](SystemLanguage.Basque.html)| Basque.  
[Belarusian](SystemLanguage.Belarusian.html)| Belarusian.  
[Bulgarian](SystemLanguage.Bulgarian.html)| Bulgarian.  
[Catalan](SystemLanguage.Catalan.html)| Catalan.  
[Chinese](SystemLanguage.Chinese.html)| Chinese.  
[Czech](SystemLanguage.Czech.html)| Czech.  
[Danish](SystemLanguage.Danish.html)| Danish.  
[Dutch](SystemLanguage.Dutch.html)| Dutch.  
[English](SystemLanguage.English.html)| English.  
[Estonian](SystemLanguage.Estonian.html)| Estonian.  
[Faroese](SystemLanguage.Faroese.html)| Faroese.  
[Finnish](SystemLanguage.Finnish.html)| Finnish.  
[French](SystemLanguage.French.html)| French.  
[German](SystemLanguage.German.html)| German.  
[Greek](SystemLanguage.Greek.html)| Greek.  
[Hebrew](SystemLanguage.Hebrew.html)| Hebrew.  
[Icelandic](SystemLanguage.Icelandic.html)| Icelandic.  
[Indonesian](SystemLanguage.Indonesian.html)| Indonesian.  
[Italian](SystemLanguage.Italian.html)| Italian.  
[Japanese](SystemLanguage.Japanese.html)| Japanese.  
[Korean](SystemLanguage.Korean.html)| Korean.  
[Latvian](SystemLanguage.Latvian.html)| Latvian.  
[Lithuanian](SystemLanguage.Lithuanian.html)| Lithuanian.  
[Norwegian](SystemLanguage.Norwegian.html)| Norwegian.  
[Polish](SystemLanguage.Polish.html)| Polish.  
[Portuguese](SystemLanguage.Portuguese.html)| Portuguese.  
[Romanian](SystemLanguage.Romanian.html)| Romanian.  
[Russian](SystemLanguage.Russian.html)| Russian.  
[SerboCroatian](SystemLanguage.SerboCroatian.html)| Serbo-Croatian.  
[Slovak](SystemLanguage.Slovak.html)| Slovak.  
[Slovenian](SystemLanguage.Slovenian.html)| Slovenian.  
[Spanish](SystemLanguage.Spanish.html)| Spanish.  
[Swedish](SystemLanguage.Swedish.html)| Swedish.  
[Thai](SystemLanguage.Thai.html)| Thai.  
[Turkish](SystemLanguage.Turkish.html)| Turkish.  
[Ukrainian](SystemLanguage.Ukrainian.html)| Ukrainian.  
[Vietnamese](SystemLanguage.Vietnamese.html)| Vietnamese.  
[ChineseSimplified](SystemLanguage.ChineseSimplified.html)| ChineseSimplified.  
[ChineseTraditional](SystemLanguage.ChineseTraditional.html)|
ChineseTraditional.  
[Hindi](SystemLanguage.Hindi.html)| Hindi.  
[Unknown](SystemLanguage.Unknown.html)| Unknown.  
[Hungarian](SystemLanguage.Hungarian.html)| Hungarian.  
  
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

