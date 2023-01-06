<!-- markdownlint-disable-next-line MD041 -->
<div align="center">
    <img src="./images/snake.png" height="160px" width="auto">
    <h3>
        <b>
            CODERNA
        </b>
    </h3>
    <p>
        Control the degree of similarity of Python code directly from the console
    </p>
</div>

<br>
<br>

<section align="center">
    <h3>
        <b>
            About
        </b>
    </h3>
    <p align="justify">
        CODERNA is a console utility designed to detect plagiarism in files with
        code written in Python. We use Levenshtein distance with some AST tips to
        measure the similarity of provided files. Detailed usage information can
        be obtained using the following command: <code>python compare.py --help</code>
    </p>
</section>

<br>
<br>

<section align="center">
    <h3>
        <b>
            Input and Output
        </b>
    </h3>
    <p align="justify">
        The tool supports the processing of many pairs of files, so the file
        format that contains information about the analyzed files is very important.
        The examples below are given when using the command:
        <code>python compare.py input.txt output.txt -f</code>
    </p>
    <br>
    <p align="justify">
        The input file must obey the following rules:
        <br>
        1. Each pair of files being compared is on a separate line;
        <br>
        2. On the i-th line, absolute paths to the corresponding files in the
        Python programming language are written separated by a space.
    </p>
    <p align="justify">
        Input file example:
        <br>
        <code>
             C:\Users\me\Desktop\old.py C:\Users\me\Desktop\new.py
             <br>
             C:\Users\me\Desktop\cheated.py C:\Users\me\Desktop\original.py
             <br>
             C:\Users\me\Documents\hello.py C:\Users\me\Documents\world.py
        </code>
    </p>
    <br>
    <p align="justify">
        The output file contains the value of the i-th metric on the i-th line.
        Remember, you can set option <code>-p</code> and write percent of
        similarity instead of ratio metric
    </p>
    <p align="justify">
        Output file example:
        <br>
        <code>
             0.67
             <br>
             1.0
             <br>
             0.2678
        </code>
    </p>
</section>

<br>
<br>

<section align="center">
    <h3>
        <b>
            Handling Errors
        </b>
    </h3>
    <p align="justify">
        It's no secret that during processing there may be any problems that we
        would like to detect. At the moment, the tool operates with errors as
        follows: if any error exists, then the program drops with an error message
        which is written to the console.
    </p>
</section>

<br>
<br>

<section align="center">
    <h3>
        <b>
            Metric
        </b>
    </h3>
    <p align="justify">
        Let's consider the i-th pair of files. Initially, both of these files
        are formatted. Due to the fact that CODERNA's work is based on the
        Levenstein algorithm, such a step allows to reduce the editorial
        distance between the lines of code by reducing probable cheating, which,
        in turn, will increase the accuracy of measuring the degree of
        similarity of programs.
        <br>
        <br>
        Then, as already noted, the Levenshtein editorial distance search
        algorithm comes into play. Using it, the corresponding value is searched
        for - let's call it <code>levenshtein_distance</code>. Adhering to the
        same logic, we will name the formatted files as follows:
        <code>fmt_lh</code> and <code>fmt_rh</code>. The further metric is
        calculated as follows: <code>1 - levenshtein_distance / max(len(fmt_lh),
        len(fmt_rh))</code>. The resulting value will be considered the
        similarity value of the text.
    </p>
</section>

<br>
<br>

<section align="center">
    <h3>
        <b>
            License
        </b>
    </h3>
    <p align="justify">
        The content provided is distributed under the MIT license. More detailed
        information about the license is located in the LICENSE file.
    </p>
</section>

<br>
<br>

<section align="center">
    <h3>
        <b>
            Credits Section
        </b>
    </h3>
    <p align="justify">
        The logo for the project was taken from the <b>Flaticon</b> service. The
        source material is available by
        <a href="https://www.flaticon.com/packs/desert-152"><i>hyperlink</i></a>
    </p>
</section>
