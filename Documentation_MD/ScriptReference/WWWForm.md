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

# WWWForm

class in UnityEngine

/

Implemented
in:[UnityEngine.UnityWebRequestModule](UnityEngine.UnityWebRequestModule.html)

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

Helper class to generate form data to post to web servers using the
[UnityWebRequest](Networking.UnityWebRequest.html) or WWW classes.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    public class WWWFormImage : [MonoBehaviour](MonoBehaviour.html)
    {  
      
        public string screenShotURL= "https://www.my-server.com/cgi-bin/screenshot.pl";  
      
        // Use this for initialization
        void Start()
        {
            StartCoroutine(UploadPNG());
        }  
      
        IEnumerator UploadPNG()
        {
            // We should only read the screen after all rendering is complete
            yield return new [WaitForEndOfFrame](WaitForEndOfFrame.html)();  
      
            // Create a texture the size of the screen, RGB24 format
            int width = [Screen.width](Screen-width.html);
            int height = [Screen.height](Screen-height.html);
            var tex = new [Texture2D](Texture2D.html)( width, height, [TextureFormat.RGB24](TextureFormat.RGB24.html), false );  
      
            // Read screen contents into the texture
            tex.ReadPixels( new [Rect](Rect.html)(0, 0, width, height), 0, 0 );
            tex.Apply();  
      
            // Encode texture into PNG
            byte[] bytes = tex.EncodeToPNG();
            Destroy( tex );  
      
            // Create a Web Form
            [WWWForm](WWWForm.html) form = new [WWWForm](WWWForm.html)();
            form.AddField("frameCount", Time.frameCount.ToString());
            form.AddBinaryData("fileUpload", bytes, "screenShot.png", "image/png");  
      
            // Upload to a cgi script
            using (var w = [UnityWebRequest.Post](Networking.UnityWebRequest.Post.html)(screenShotURL, form))
            {
                yield return w.SendWebRequest();
                if (w.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html)) {
                    print(w.error);
                }
                else {
                    print("Finished Uploading Screenshot");
                }
            }
        }
    }
    

Here is a sample script that retrieves the high scores stored in a table in an
SQL database.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    public class WWWFormScore : [MonoBehaviour](MonoBehaviour.html)
    {
        string highscore_url = "https://www.my-site.com/highscores.pl";
        string playName = "Player 1";
        int score = -1;  
      
        // Use this for initialization
        IEnumerator Start()
        {
            // Create a form object for sending high score data to the server
            [WWWForm](WWWForm.html) form = new [WWWForm](WWWForm.html)();  
      
            // Assuming the perl script manages high scores for different games
            form.AddField( "game", "MyGameName" );  
      
            // The name of the player submitting the scores
            form.AddField( "playerName", playName );  
      
            // The score
            form.AddField( "score", score );  
      
            // Create a download object
            var download = [UnityWebRequest.Post](Networking.UnityWebRequest.Post.html)(highscore_url, form);  
      
            // Wait until the download is done
            yield return download.SendWebRequest();  
      
            if (download.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
            {
                print( "[Error](PackageManager.Error.html) downloading: " + download.error );
            }
            else
            {
                // show the highscores
                [Debug.Log](Debug.Log.html)(download.downloadHandler.text);
            }
        }
    }
    

Here is a sample Perl script that processes the high scores stored in a table
in an SQL database.

    
    
    #!/usr/bin/perl
    # The SQL database needs to have a table called highscores
    # that looks something like this:
    #
    #   CREATE TABLE highscores (
    #     game varchar(255) NOT NULL,
    #     player varchar(255) NOT NULL,
    #     score integer NOT NULL
    #   );
    #
    use strict;
    use CGI;
    use DBI;  
      
    # Read form data etc.
    my $cgi = new CGI;  
      
    # The results from the high score script will be in plain text
    print $cgi->header("text/plain");  
      
    my $game = $cgi->param('game');
    my $playerName = $cgi->param('playerName');
    my $score = $cgi->param('score');  
      
    exit 0 unless $game; # This parameter is required  
      
    # Connect to a database
    my $dbh = DBI->connect( 'DBI:mysql:databasename', 'username', 'password' )
        || die "Could not connect to database: $DBI::errstr";  
      
    # Insert the player score if there are any
    if( $playerName && $score) {
        $dbh->do( "insert into highscores (game, player, score) values(?,?,?)",
            undef, $game, $playerName, $score );
    }  
      
    # Fetch the high scores
    my $sth = $dbh->prepare(
        'SELECT player, score FROM highscores WHERE game=? ORDER BY score desc LIMIT 10' );
    $sth->execute($game);
    while (my $r = $sth->fetchrow_arrayref) {
        print join(':',@$r),"\n"
    }

### Properties

[data](WWWForm-data.html)| (Read Only) The raw data to pass as the POST
request body when sending the form.  
---|---  
[headers](WWWForm-headers.html)| (Read Only) Returns the correct request
headers for posting the form using the WWW class.  
  
### Constructors

[WWWForm](WWWForm-ctor.html)| Creates an empty WWWForm object.  
---|---  
  
### Public Methods

[AddBinaryData](WWWForm.AddBinaryData.html)| Add binary data to the form.  
---|---  
[AddField](WWWForm.AddField.html)| Add a simple field to the form.  
  
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

